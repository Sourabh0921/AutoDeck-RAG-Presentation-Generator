import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)
from src.retrieval.retriever import (
    Retriever
)

retriever = Retriever()

results = retriever.search(
    "Federal Agency Programs"
)

for doc in results:

    print("="*50)

    print(
        doc.metadata
    )

    print(
        doc.page_content[:500]
    )