import os
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as LangchainPinecone
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Correct imports for embeddings
from langchain_community.embeddings import SentenceTransformerEmbeddings  # Corrected import
from langchain_huggingface import HuggingFaceEmbeddings  # New import


def get_vectorstore():
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    google_api_key = os.getenv("GOOGLE_API_KEY")

    if not pinecone_api_key:
        raise ValueError("🚨 Pinecone API key is missing!")

    # Initialize Pinecone client
    pc = Pinecone(api_key=pinecone_api_key)

    # Use SentenceTransformerEmbeddings
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Must match your existing index name
    return LangchainPinecone.from_existing_index("ecom-memory", embeddings)
