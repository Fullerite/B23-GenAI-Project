## Setup
1. Install requirements: `pip install -r requirements.txt`
2. Configure environment: Create a `.env` file with `LLM_API_URL`.
3. Configure the `config.yaml` file for your use.
4. Local Fallback: For CPU-only reproduction, install Ollama and run `ollama run qwen3:1.7b`.

## 1. Data Pipeline
To scrape the documentation and convert it to Markdown:
```
python3 -m src.scraper.scraper
```

## 2. Vector Store
To process the Markdown files and populate the vector store:
```
python3 -m src.vector_store.inject
```

*Note: Ensure `use_context_injection: false` is set in `config.yaml` for baseline reproduction.*

## 3. Evaluation
To run the 50-question benchmark and generate the performance report:
`python3 -m scripts.evaluate`

## Reproducibility Note
**Retriever:** Purely deterministic. A static local vector store (`ChromaDB`) and a fixed embedding model (`all-MiniLM-L6-v2`).
**Generator:** Variance is suppressed by pinning the random seed to `42` and fixing the sampling temperature to `0.3`
