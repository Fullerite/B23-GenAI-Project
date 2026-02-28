import json
import pandas as pd
from tqdm import tqdm
from src.llm.wrapper import LLMClient
from src.vector_store.db import get_vector_collection
from scripts.misc import load_config


config = load_config()
LLM_API_URL = config["model"]["llm_api_url"]
DATA_FILE = config["data"]["benchmark_data_path"]
OUTPUT_FILE = config["data"]["benchmark_results_path"]
MODEL_ID = config["model"]["model_id"]
RETRIEVAL_TOP_K = config["model"]["retrieval_top_k"]


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
        response = client.generate_response(
            messages=[{"role": "user", "content": prompt}]
        )
        score = "".join(filter(str.isdigit, response))
        return int(score[0]) if score else 1
    except:
        return 1


def run_benchmark():
    with open(DATA_FILE, "r") as f:
        test_cases = json.load(f)

    collection = get_vector_collection()
    llm_client = LLMClient(
        base_url=LLM_API_URL,
        model=MODEL_ID
    )

    results = []

    for case in tqdm(test_cases, desc="Evaluating"):
        question = case["question"]
        answer = case["answer"]
        truth_source = case["source"]

        search_res = collection.query(query_texts=[question], n_results=RETRIEVAL_TOP_K)
        chunks = search_res["documents"][0]
        metadatas = search_res["metadatas"][0]

        retrieved_sources = [meta["id"].rsplit("_chunk_", 1)[0] for meta in metadatas]
        recall_score = 1 if truth_source in retrieved_sources else 0

        generated_answer = llm_client.generate_response(
            messages=[{"role": "user", "content": question}],
            context_chunks=chunks
        )

        faithfulness_score = evaluate_answer(
            llm_client,
            question,
            generated_answer,
            answer)

        clean_truth = truth_source.replace(".md", "").strip().lower()
        clean_gen = generated_answer.lower()
        citation_score = 1 if clean_truth in clean_gen else 0
                
        results.append({
            "Question": question,
            "Ground Truth": answer,
            "Truth Source": truth_source,
            "Generated Answer": generated_answer,
            "Faithfulness Score": faithfulness_score,
            f"Recall@{RETRIEVAL_TOP_K}": recall_score,
            "Citation Accuracy": citation_score
        })

    df = pd.DataFrame(results)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Benchmark complete. Report saved to {OUTPUT_FILE}")
    print(f"Avg Faithfulness: {df['Faithfulness Score'].mean():.2f} / 5.0")
    print(f"Retrieval Recall@{RETRIEVAL_TOP_K}: {df[f'Recall@{RETRIEVAL_TOP_K}'].mean() * 100:.1f}%")
    print(f"Citation Accuracy: {df['Citation Accuracy'].mean() * 100:.1f}%")


if __name__ == "__main__":
    run_benchmark()
