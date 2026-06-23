import json

from langchain_core.documents import Document

from langchain_community.vectorstores import FAISS

from src.embeddings.embedding_model import (
    EmbeddingModel
)


class FAISSBuilder:

    def create_index(
        self,
        chunks_json_path,
        save_path
    ):

        with open(
            chunks_json_path,
            "r",
            encoding="utf-8"
        ) as f:

            chunks = json.load(f)
        # Test Mode
        # import time

        # start = time.time()
        # chunks = chunks[:1000]
        # end = time.time()

        # print((end-start)/60)

        # print(f"Testing with {len(chunks)} chunks")
        print(len(chunks))
        documents = []

        for idx, chunk in enumerate(chunks):

            if idx % 500 == 0:
                print(
                    f"Processing chunk {idx}"
                )

            documents.append(
                Document(
                    page_content=chunk["text"],
                    metadata={
                        "chunk_id":
                        chunk["chunk_id"],

                        "doc_id":
                        chunk["doc_id"],

                        "source": 
                        chunk["doc_id"]
                    }
                )
            )

        embedding_model = (
            EmbeddingModel()
            .get_embedding_model()
        )

        vectorstore = (
            FAISS.from_documents(
                documents,
                embedding_model
            )
        )

        vectorstore.save_local(
            save_path
        )

        print(
            "FAISS Index Saved Successfully"
        )