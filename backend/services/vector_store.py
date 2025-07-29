from langchain.vectorstores import Chroma
from backend.services.embed import get_embedding_model
import os

VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "./chroma_db")

def get_vector_store(docs):
    embedder = get_embedding_model()
    return Chroma.from_documents(docs, embedding=embedder, persist_directory=VECTOR_DB_PATH)

def load_vector_store():
    embedder = get_embedding_model()
    return Chroma(persist_directory=VECTOR_DB_PATH, embedding_function=embedder)
