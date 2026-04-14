## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Configure environment: Create a `.env` file with `LLM_API_URL`.
3. Configure the `configs/config.yaml` file for your use (see below).
4. Local Fallback: For CPU-only reproduction, install Ollama and run `ollama run qwen3:1.7b`.

### Local Fallback
For CPU-only reproduction, install Ollama and run the model you need.

First, start the Ollama server in the background:
```
ollama serve
```

Then, in a new terminal, pull the model:
```
ollama pull qwen3:1.7b
```

In your `.env` file, set `LLM_API_URL=http://localhost:11434`.

### Key configuration parameters
- `model.model_id`: the name of the LLM (e.g., `qwen3:1.7b`)
- `model.llm_api_url`: the LLM API endpoint
- `model.collection_name`: "docs_final" (or any name; the pipeline uses this collection)
- `data.benchmark_data_path`: "data/benchmark/benchmark_data_multilabel.json"
- `data.benchmark_results_path`: "data/benchmark/benchmark_report_final.csv"
- `model.retrieval_top_k`: 5

## 1. Data Pipeline
To scrape the documentation and convert it to markdown:
```
python3 -m src.scraper.scraper
```

## 2. Vector Store
To build the final vector store with **token‑based splitting + prefix injection**:
```
python3 -m src.vector_store.ingest
```
This creates the collection defined in `config.yaml`.  
The ingestion uses `tokens_per_chunk=192` and `chunk_overlap=20` to eliminate truncation holes.

## 3. Evaluation
To run the 50‑query multi‑label benchmark and generate the performance report:
```
python3 -m scripts.evaluate
```
The script performs hybrid BM25+vector retrieval with Reciprocal Rank Fusion (RRF) and outputs:
- Recall@5, Citation Accuracy, Faithfulness (1–5)
- Results saved to the path set in `config.yaml`

## 4. Interactive Demo
To launch the Streamlit chat assistant (uses the same final retrieval pipeline):
```
streamlit run app.py
```

## Reproducibility Note
**Retriever:** Deterministic. Uses a static local ChromaDB collection, a fixed embedding model (`all-MiniLM-L6-v2`), and a fixed BM25 tokenizer.
**Generator:** Variance suppressed by setting random seed `42` and sampling temperature `0.3` in the LLM client.
**Data:** The benchmark dataset includes multiple valid sources per query (inheritance‑aware). The JSON file is located in `data/benchmark/benchmark_data_multilabel.json`.
