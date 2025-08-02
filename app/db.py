#This code is part of a FastAPI application that interacts with ChromaDB to manage scheme chunks.
# It provides functions to add scheme chunks and search for them based on language and embeddings.

# Necessary imports
import chromadb
from chromadb.config import Settings

# Created a ChromaDB client with in-memory storage
# This is useful for testing or when persistent storage is not required.
chroma_client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory=None  # in-memory
))

# Created a collection for schemes
# This collection will store scheme chunks with their embeddings and metadata.
collection = chroma_client.get_or_create_collection(
    name="schemes",
    metadata={"hnsw:space": "cosine"}
)

# Function to add a scheme chunk to the collection
# It takes an ID, text, embedding, scheme ID, and language as parameters.
def add_scheme_chunk(id: str, text: str, embedding: list[float], scheme_id: str, lang: str):
    collection.add(
        ids=[id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{
            "scheme_id": scheme_id,
            "lang": lang
        }]
    )

# Function to search for scheme chunks based on a query embedding and language
# It returns the top K results that match the query embedding and language.
def search_chunks(query_embedding: list[float], lang: str, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={"lang": lang}
    )
    return results
