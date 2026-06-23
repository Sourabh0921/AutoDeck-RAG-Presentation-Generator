from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.preprocessing.cleaning import TextCleaner


class DocumentChunker:

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200
        )

    def create_chunks(self, documents):

        chunks = []

        for doc in documents:

            doc_id = doc["doc_id"]

            text = doc["content"]
            clean_text = TextCleaner.clean_text(text)
            split_texts = self.splitter.split_text(clean_text)

            for idx, chunk in enumerate(split_texts):

                chunks.append(
                    {
                        "chunk_id": f"{doc_id}_{idx}",
                        "doc_id": doc_id,
                        "text": chunk
                    }
                )

        return chunks