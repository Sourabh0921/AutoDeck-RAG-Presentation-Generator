# from tika import parser

# file_path = r"C:\AutoDeck_rag_system\AutoDeck_RAG_System\Dataset\Dataset\train\2C45NWO7FMTDRTBBR6FA442OZKSCLGZZ.ppt"

# parsed = parser.from_file(file_path)

# print(parsed["content"])
import sys
import os

project_root = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.append(project_root)

from src.ingestion.document_loader import PPTDocumentLoader

loader = PPTDocumentLoader()

documents = loader.process_folder(
    r"C:\AutoDeck_rag_system\AutoDeck_RAG_System\Dataset\Dataset\val"
)

loader.save_documents(
    documents,
    r"data\processed\documents\val_documents.json"
)

print(len(documents))