import os
from tqdm import tqdm
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    SentenceTransformersTokenTextSplitter
)
from src.vector_store.db import get_vector_collection
from scripts.misc import load_config

config = load_config()
DATA_DIR = config["data"]["main_data_dir"]

ABLATIONS = [
    {"name": "docs_no_context", "type": "no_context"},
    {"name": "docs_prefix", "type": "prefix"},
    {"name": "docs_suffix", "type": "suffix"},
    {"name": "docs_adaptive", "type": "adaptive"}
]

def load_and_chunk_files_for_ablation(ablation_type):
    headers_to_split_on = [("#", "h1"), ("##", "h2"), ("###", "h3")]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

    token_splitter = SentenceTransformersTokenTextSplitter(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        tokens_per_chunk=192,
        chunk_overlap=20
    )

    final_chunks = []

    if not os.path.exists(DATA_DIR):
        print(f"Data directory not found at {DATA_DIR}")
        return []

    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".md")]

    for filename in tqdm(files, desc=f"Processing ({ablation_type})"):
        path = os.path.join(DATA_DIR, filename)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        header_splits = markdown_splitter.split_text(text)
        splits = token_splitter.split_documents(header_splits)

        for idx, doc in enumerate(splits):
            if len(doc.page_content) < 50:
                continue

            sections = [doc.metadata.get(h) for h in ["h1", "h2", "h3"] if doc.metadata.get(h)]
            context_header = " > ".join(sections)
            header_str = f"Context: {context_header}\n" if sections else ""
            source_str = f"Source: {filename}\n"
            separator = "---\n"

            if ablation_type == "no_context":
                doc.page_content = f"{source_str}{separator}{doc.page_content}"
            elif ablation_type == "prefix":
                doc.page_content = f"{header_str}{source_str}{separator}{doc.page_content}"
            elif ablation_type == "suffix":
                doc.page_content = f"{doc.page_content}\n{separator}{header_str}{source_str}"
            elif ablation_type == "adaptive":
                deepest = sections[-1] if sections else ""
                name_to_match = deepest.replace("Class ", "").replace("Interface ", "").lower()
                preview = doc.page_content[:200].lower()
                if name_to_match and name_to_match in preview:
                    doc.page_content = f"{source_str}{separator}{doc.page_content}"
                else:
                    doc.page_content = f"{header_str}{source_str}{separator}{doc.page_content}"

            doc.metadata["id"] = f"{filename}_chunk_{idx}"
            final_chunks.append(doc)

    return final_chunks

def run_ablations():
    print(f"Starting Ablation Ingestion for {len(ABLATIONS)} configurations...\n")

    for config_item in ABLATIONS:
        col_name = config_item["name"]
        abl_type = config_item["type"]

        print(f"--- Building Collection: {col_name} ---")
        collection = get_vector_collection(col_name)
        chunks = load_and_chunk_files_for_ablation(abl_type)

        if not chunks:
            print("WARNING: No chunks generated")
            continue

        batch_size = 500
        for i in tqdm(range(0, len(chunks), batch_size), desc="Batch Upsert"):
            batch = chunks[i : i + batch_size]
            collection.upsert(
                ids=[doc.metadata["id"] for doc in batch],
                documents=[doc.page_content for doc in batch],
                metadatas=[doc.metadata for doc in batch]
            )
        print("\n")

if __name__ == "__main__":
    run_ablations()
