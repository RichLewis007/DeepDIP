from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
import os

def get_embedding_model():
    model_type = os.getenv("EMBEDDING_MODEL", "sentence")

    if model_type == "openai":
        return OpenAIEmbeddings()
    else:
        return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
