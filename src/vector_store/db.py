import os
import chromadb
from chromadb import EmbeddingFunction, Documents, Embeddings
from sentence_transformers import SentenceTransformer


DB_PATH = os.path.join(os.getcwd(), "chroma_db")
COLLECTION_NAME = "docs"
MODEL_NAME = "all-MiniLM-L6-v2"

class SentenceTransformersEmbeddingFunction(EmbeddingFunction):
    def __init__(self):
        print(f"Loading embedding model: {MODEL_NAME}...")
        self.model = SentenceTransformer(MODEL_NAME)

    def __call__(self, input: Documents) -> Embeddings:
        vectors = self.model.encode(input)
        return vectors.tolist()


def get_vector_collection():
    embedding_function = SentenceTransformersEmbeddingFunction()
    client = chromadb.PersistentClient(path=DB_PATH)

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=embedding_function,
        metadata={"hnsw:space": "cosine"}
    )
