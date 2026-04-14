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
COLLECTION_NAME = config["model"]["collection_name"]


def load_and_chunk_files():
    headers_to_split_on = [("#", "h1"), ("##", "h2"), ("###", "h3")]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    token_splitter = SentenceTransformersTokenTextSplitter(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        tokens_per_chunk=192,
        chunk_overlap=20
    )

    final_chunks = []

    if not os.path.exists(DATA_DIR):
        print(f"ERROR: Data directory not found at {DATA_DIR}")
        return []

    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".md")]
    print(f"Found {len(files)} markdown files")

    for filename in tqdm(files, desc="Processing files"):
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

            doc.page_content = f"{header_str}{source_str}{separator}{doc.page_content}"
            doc.metadata["id"] = f"{filename}_chunk_{idx}"

            final_chunks.append(doc)

    return final_chunks


def run_ingest():
    print(f"Building collection: {COLLECTION_NAME}")
    collection = get_vector_collection(collection_name=COLLECTION_NAME)
    chunks = load_and_chunk_files()

    if not chunks:
        print("WARNING: No chunks generated")
        return

    batch_size = 500
    for i in tqdm(range(0, len(chunks), batch_size), desc="Batch Upsert"):
        batch = chunks[i : i + batch_size]
        collection.upsert(
            ids=[doc.metadata["id"] for doc in batch],
            documents=[doc.page_content for doc in batch],
            metadatas=[doc.metadata for doc in batch]
        )
    print("Ingestion complete")


if __name__ == "__main__":
    run_ingest()
