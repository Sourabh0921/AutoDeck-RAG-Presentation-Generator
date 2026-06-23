import json
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from src.preprocessing.text_splitter import DocumentChunker

with open(
    "data/processed/documents/extracted_documents.json",
    "r",
    encoding="utf-8"
) as f:

    documents = json.load(f)

chunker = DocumentChunker()

chunks = chunker.create_chunks(documents)

print("Total Chunks :", len(chunks))

with open(
    "data/processed/chunks/all_chunks.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        chunks,
        f,
        indent=4,
        ensure_ascii=False
    )