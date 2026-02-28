import os
from tqdm import tqdm
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from src.vector_store.db import get_vector_collection
from scripts.misc import load_config


config = load_config()
DATA_DIR = config["data"]["main_data_dir"]
USE_CONTEXT_INJECTION = config["model"]["use_context_injection"]
if USE_CONTEXT_INJECTION:
    print("Chunking with context injection enabled...")
else:
    print("Chunking without context injection...")


def load_and_chunk_files():
    headers_to_split_on = [("#", "h1"), ("##", "h2"), ("###", "h3")]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    recursive_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
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
        recursive_splits = recursive_splitter.split_documents(header_splits)

        for idx, doc in enumerate(recursive_splits):
            if len(doc.page_content) < 50:
                continue

            if USE_CONTEXT_INJECTION:
                sections = [doc.metadata.get(h) for h in ["h1", "h2", "h3"] if doc.metadata.get(h)]
                context_header = " > ".join(sections)
                doc.page_content = f"Context: {context_header}\nSource: {filename}\n---\n{doc.page_content}"
            else:
                doc.page_content = f"Source: {filename}\n---\n{doc.page_content}"

            doc.metadata["id"] = f"{filename}_chunk_{idx}"

            final_chunks.append(doc)

    return final_chunks


def run_ingest():
    collection = get_vector_collection()
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


if __name__ == "__main__":
    run_ingest()
