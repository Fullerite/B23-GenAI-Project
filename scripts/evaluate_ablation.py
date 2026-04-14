import re
import json
import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from src.llm.wrapper import LLMClient
from rank_bm25 import BM25Okapi
from src.vector_store.db import get_vector_collection
from scripts.misc import load_config


config = load_config()
LLM_API_URL = config["model"]["llm_api_url"]
DATA_FILE = config["data"]["benchmark_data_path"]
MODEL_ID = config["model"]["model_id"]
RETRIEVAL_TOP_K = config["model"]["retrieval_top_k"]

COLLECTIONS = [
    "docs_no_context",
    "docs_prefix",
    "docs_suffix",
    "docs_adaptive",
    "docs_injected"
]

OUTPUT_DIR = "data/benchmark/ablation"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def evaluate_answer(client, question, generated_answer, ground_truth):
    prompt = f"""
    # Task
    You are an LLM judge. Grade the accuracy of the generated answer compared to the ground truth.

    # Criteria
    1 - Completely wrong or irrelevant.
    3 - Partially correct but missing key details.
    5 - Correct, complete, and informative.

    # Context
    Question: "{question}"
    Ground Truth: "{ground_truth}"
    Generated Answer: "{generated_answer}"

    # Output format    
    Output ONLY a single number (1, 2, 3, 4, or 5). Do not write any other text or explanations.
    """.strip()

    try:
        response = client.generate_response(messages=[{"role": "user", "content": prompt}])
        score = "".join(filter(str.isdigit, response))
        return int(score[0]) if score else 1
    except:
        return 1


def run_benchmark_for_collection(collection_name):
    print(f"\n{'='*60}")
    print(f"Evaluating collection: {collection_name}")
    print('='*60)

    collection = get_vector_collection(collection_name)
    llm_client = LLMClient(base_url=LLM_API_URL, model=MODEL_ID)

    all_data = collection.get(include=["documents", "metadatas"])
    all_docs = all_data["documents"]
    all_metas = all_data["metadatas"]

    def _tokenize(text):
        return re.findall(r"\w+", text.lower())

    tokenized_corpus = [_tokenize(doc) for doc in all_docs]
    bm25 = BM25Okapi(tokenized_corpus)

    with open(DATA_FILE, "r") as f:
        test_cases = json.load(f)

    results = []
    for case in tqdm(test_cases, desc="Evaluating"):
        question = case["question"]
        answer = case["answer"]
        primary_truth_source = case["source"]
        valid_sources = case.get("valid_sources", [primary_truth_source])

        vec_res = collection.query(query_texts=[question], n_results=20)
        vec_ids = vec_res["ids"][0]

        q_tokens = _tokenize(question)
        bm25_scores = bm25.get_scores(q_tokens)
        top_20_bm25_idx = np.argsort(bm25_scores)[::-1][:20]
        bm25_ids = [all_metas[i]["id"] for i in top_20_bm25_idx]

        rrf_scores = {}
        for rank, doc_id in enumerate(vec_ids):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1.0 / (10 + rank)
        for rank, doc_id in enumerate(bm25_ids):
            rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1.0 / (10 + rank)

        top_ids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)[:5]

        id_to_idx = {meta["id"]: i for i, meta in enumerate(all_metas)}
        pool_docs = []
        for doc_id in top_ids:
            idx = id_to_idx[doc_id]
            pool_docs.append(all_docs[idx])

        retrieved_sources = [meta["id"].rsplit("_chunk_", 1)[0] for meta in all_metas if meta["id"] in top_ids]
        recall_score = 1 if any(src in retrieved_sources for src in valid_sources) else 0

        generated_answer = llm_client.generate_response(
            messages=[{"role": "user", "content": question}],
            context_chunks=pool_docs
        )

        faithfulness_score = evaluate_answer(llm_client, question, generated_answer, answer)
        clean_gen = generated_answer.lower()
        citation_score = 1 if any(src.replace(".md", "").strip().lower() in clean_gen for src in valid_sources) else 0

        results.append({
            "Question": question,
            "Ground Truth": answer,
            "Truth Source": valid_sources,
            "Generated Answer": generated_answer,
            "Faithfulness Score": faithfulness_score,
            f"Recall@{RETRIEVAL_TOP_K}": recall_score,
            "Citation Accuracy": citation_score
        })

    df = pd.DataFrame(results)
    output_path = os.path.join(OUTPUT_DIR, f"{collection_name}_results.csv")
    df.to_csv(output_path, index=False)

    print(f"\n--- Results for {collection_name} ---")
    print(f"Saved to: {output_path}")
    print(f"Avg Faithfulness: {df['Faithfulness Score'].mean():.2f} / 5.0")
    print(f"Retrieval Recall@{RETRIEVAL_TOP_K}: {df[f'Recall@{RETRIEVAL_TOP_K}'].mean() * 100:.1f}%")
    print(f"Citation Accuracy: {df['Citation Accuracy'].mean() * 100:.1f}%")


def main():
    for col in COLLECTIONS:
        run_benchmark_for_collection(col)


if __name__ == "__main__":
    main()
