import os

from dotenv import load_dotenv

# from langchain_google_genai import (
#     GoogleGenerativeAIEmbeddings
# )

load_dotenv()


from langchain_huggingface import (
    HuggingFaceEmbeddings
)


class EmbeddingModel:

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            # model_name="BAAI/bge-small-en-v1.5"
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def get_embedding_model(self):

        return self.embeddings