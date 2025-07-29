from backend.services.vector_store import load_vector_store
from backend.services.llm_chain import get_llm_agent

def answer_query(query: str):
    vectordb = load_vector_store()
    docs = vectordb.similarity_search(query)
    agent = get_llm_agent()
    answer = agent.run(input=query)
    return {"query": query, "answer": answer, "source_count": len(docs)}
