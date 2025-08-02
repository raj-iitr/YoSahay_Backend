# This code is part of a FastAPI application that interacts with OpenAI's API to generate text embeddings.
# It provides a function to embed text using OpenAI's embedding model.

# Necessary imports
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")  # store in .env

EMBED_MODEL = "text-embedding-3-small"

# Function to embed text using OpenAI's API
# It returns a list of floats representing the text embedding.
def embed_text(text: str) -> list[float]:
    try:
        response = openai.Embedding.create(
            input=text,
            model=EMBED_MODEL
        )
        return response["data"][0]["embedding"]
    except Exception as e:
        print(f"[Embedding Error] {e}")
        return []
