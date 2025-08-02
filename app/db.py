# app/db.py

import os
import chromadb

# Render requires persistent storage under /persistent
persist_dir = os.getenv("CHROMA_DIR", "/persistent/chroma_data")

chroma_client = chromadb.PersistentClient(path=persist_dir)

collection = chroma_client.get_or_create_collection(
    name="schemes"
)

print("ChromaDB client initialized and collection is ready.")

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

def search_chunks(query_embedding: list[float], lang: str, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where={"lang": lang}
    )
    return results


