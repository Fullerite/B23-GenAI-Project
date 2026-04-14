import os
import re
import numpy as np
import streamlit as st
from dotenv import load_dotenv
from rank_bm25 import BM25Okapi
from src.vector_store.db import get_vector_collection
from src.llm.wrapper import LLMClient
from scripts.misc import load_config

load_dotenv()
config = load_config()
LLM_API_URL = config["model"]["llm_api_url"]
MODEL_ID = config["model"]["model_id"]
RETRIEVAL_TOP_K = config["model"]["retrieval_top_k"]
COLLECTION_NAME = config["model"].get("collection_name", "docs_final")

def get_routing_decision(query):    
    query = query.lower().strip()
    tech_pattern = r"\b(cache|request|engine|iter|json|promise|linkedlist|interface|class|api|ttl|queue|component|module|router|middleware|encode|decode|storage|session|config|prop|method|type|arg|param|return|value|function|object|const|var)\b"
    if re.search(tech_pattern, query):
        return "rag"
    chat_pattern = r"\b(hi|hello|feel|mood|weather|sentient|conscious|joke|poem|story|love|hate|life|robot|ai|yourself|who|what are you)\b"
    if re.search(chat_pattern, query):
        return "chat"
    question_starters = ("what", "how", "why", "explain", "define", "show", "list", "can", "does", "is", "where", "give")
    if query.startswith(question_starters):
        return "rag"
    if len(query.split()) < 4:
        return "chat"
    return "rag"

st.set_page_config(page_title="V4Fire Docs Bot", layout="wide")
st.title("V4Fire Core Documentation Assistant")

with st.sidebar:
    st.subheader("Conversation Info")
    if "history" in st.session_state:
        st.write(f"Messages in memory: {len(st.session_state.history)}")

if "history" not in st.session_state:
    st.session_state.history = []

if "vector_db" not in st.session_state:
    try:
        st.session_state.vector_db = get_vector_collection(collection_name=COLLECTION_NAME)
        all_data = st.session_state.vector_db.get(include=["documents", "metadatas"])
        st.session_state.all_docs = all_data["documents"]
        st.session_state.all_metas = all_data["metadatas"]
        tokenized_corpus = [re.findall(r"\w+", doc.lower()) for doc in st.session_state.all_docs]
        st.session_state.bm25 = BM25Okapi(tokenized_corpus)
        st.success(f"Local vector DB '{COLLECTION_NAME}' loaded")
    except Exception as e:
        st.error(f"Failed to load DB: {e}")

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question about the documentation..."):
    if not LLM_API_URL:
        st.error("LLM_API_URL not set in environment variables.")
        st.stop()

    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")

        try:
            llm = LLMClient(base_url=LLM_API_URL, model=MODEL_ID)
            
            route = get_routing_decision(prompt)
            context_chunks = []
            
            if route == "rag":
                with st.status("Searching Knowledge Base...", expanded=False) as status:
                    vec_res = st.session_state.vector_db.query(
                        query_texts=[prompt],
                        n_results=20
                    )
                    vec_ids = vec_res["ids"][0]
                    q_tokens = re.findall(r"\w+", prompt.lower())
                    bm25_scores = st.session_state.bm25.get_scores(q_tokens)
                    top_20_bm25_idx = np.argsort(bm25_scores)[::-1][:20]
                    bm25_ids = [st.session_state.all_metas[i]["id"] for i in top_20_bm25_idx]
                    rrf_scores = {}
                    for rank, doc_id in enumerate(vec_ids):
                        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1.0 / (10 + rank)
                    for rank, doc_id in enumerate(bm25_ids):
                        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + 1.0 / (10 + rank)
                    top_ids = sorted(rrf_scores.keys(), key=lambda x: rrf_scores[x], reverse=True)[:RETRIEVAL_TOP_K]
                    id_to_idx = {meta["id"]: i for i, meta in enumerate(st.session_state.all_metas)}
                    for doc_id in top_ids:
                        idx = id_to_idx[doc_id]
                        context_chunks.append(st.session_state.all_docs[idx])
                    status.write(f"Found {len(context_chunks)} relevant sections.")
                    status.update(label="Context Retrieved", state="complete")

            recent_history = st.session_state.history[-5:]
            
            response_text = llm.generate_response(
                messages=recent_history,
                context_chunks=context_chunks if route == "rag" else None
            )
            
            message_placeholder.markdown(response_text)
            st.session_state.history.append({"role": "assistant", "content": response_text})

            if route == "rag" and context_chunks:
                with st.expander("View Sources"):
                    for i, chunk in enumerate(context_chunks):
                        st.caption(f"**Chunk {i+1}**")
                        st.text(chunk[:300] + "...")

        except Exception as e:
            message_placeholder.error(f"An error occurred: {e}")
