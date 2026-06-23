from langchain_community.vectorstores import FAISS

from src.embeddings.embedding_model import (
    EmbeddingModel
)


class Retriever:

    def __init__(self):

        embeddings = (
            EmbeddingModel()
            .get_embedding_model()
        )

        self.db = FAISS.load_local(
            "vector_store/faiss_index",
            embeddings,
            allow_dangerous_deserialization=True
        )

    def search(
        self,
        query,
        k=5
    ):

        return self.db.similarity_search(
            query,
            k=k
        )