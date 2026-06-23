import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from src.embeddings.embedding_model import (
    EmbeddingModel
)

model = (
    EmbeddingModel()
    .get_embedding_model()
)

vector = model.embed_query(
    "Artificial Intelligence in Healthcare"
)

print(
    "Vector Length :",
    len(vector)
)