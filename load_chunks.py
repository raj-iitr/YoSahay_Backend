# load_chunks.py

import uuid
from app.db import add_scheme_chunk
from app.embedder import embed_text

def load_scheme(file_path: str, scheme_id: str, lang: str):
    with open(file_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    chunks = split_text(full_text, max_len=300)
    
    for chunk in chunks:
        embedding = embed_text(chunk)
        if not embedding:
            continue

        chunk_id = str(uuid.uuid4())
        add_scheme_chunk(chunk_id, chunk, embedding, scheme_id, lang)

    print(f"✅ Loaded {len(chunks)} chunks for '{scheme_id}' [{lang}]")

def split_text(text: str, max_len: int = 300) -> list[str]:
    # Simple chunking by paragraph or newline
    lines = text.split("\n")
    chunks = []
    buffer = ""
    
    for line in lines:
        if len(buffer + line) < max_len:
            buffer += line.strip() + " "
        else:
            chunks.append(buffer.strip())
            buffer = line.strip() + " "

    if buffer.strip():
        chunks.append(buffer.strip())
    return chunks
    
    
if __name__ == "__main__":
    load_scheme("docs\pmkisaan.txt", scheme_id="pmkisan", lang="hi")
