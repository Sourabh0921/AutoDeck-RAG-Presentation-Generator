# AutoDeck AI Presentation Generator

## Overview

AutoDeck AI Presentation Generator is an end-to-end Retrieval-Augmented Generation (RAG) system that automatically creates structured presentations from user-provided topics.

The system retrieves relevant content from a PowerPoint document knowledge base, generates presentation outlines, creates slide content, and returns presentation-ready JSON outputs.

---

## Features

* PowerPoint document ingestion
* Text extraction using Apache Tika
* Text chunking and preprocessing
* Semantic search using FAISS
* HuggingFace Embeddings
* Retrieval-Augmented Generation (RAG)
* Presentation outline generation
* Slide content generation
* FastAPI backend
* Streamlit frontend
* JSON export
* Source attribution and grounding

---

## System Architecture

PPT Files
→ Text Extraction
→ Chunking
→ Embeddings
→ FAISS Vector Store
→ Retriever
→ Groq LLM
→ Outline Generation
→ Slide Generation
→ Presentation JSON
→ FastAPI
→ Streamlit

---

## Tech Stack

### Backend

* Python
* FastAPI
* LangChain

### Vector Database

* FAISS

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### LLM

* Groq
* openai/gpt-oss-120b

### Frontend

* Streamlit

---

## Project Structure

src/
├── ingestion/
├── chunking/
├── embeddings/
├── vectordb/
├── retrieval/
├── chains/
├── schemas/
├── utils/

outputs/
├── json_outputs/
└── logs/

vector_store/

---

## API Endpoint

POST /api/generate

Request:

{
"topic": "Applications of AI in Healthcare"
}

Response:

{
"slides": [
{
"title": "...",
"bullets": ["..."],
"source": "document_id"
}
]
}

---

## How To Run

### Install Dependencies

pip install -r requirements.txt

### Run FastAPI

uvicorn app:app --reload

### Run Streamlit

streamlit run app_streamlit.py

---

## Future Improvements

* Hybrid Search
* Re-ranking
* PowerPoint Export (.pptx)
* Multi-Agent Presentation Generation
* Evaluation Metrics Dashboard
