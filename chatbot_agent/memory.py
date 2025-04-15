from langchain.memory import VectorStoreRetrieverMemory
from .vectorstore import get_vectorstore

def get_memory():
    vectorstore = get_vectorstore()
    return VectorStoreRetrieverMemory(retriever=vectorstore.as_retriever())
