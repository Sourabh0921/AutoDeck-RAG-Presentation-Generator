import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from src.vectordb.create_index import (
    FAISSBuilder
)

builder = FAISSBuilder()

builder.create_index(
    chunks_json_path=
    r"data/processed/chunks/all_chunks.json",

    save_path=
    r"vector_store/faiss_index"
)