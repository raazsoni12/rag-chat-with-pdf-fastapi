# 📄 RAG Chat with PDF Assistant (FastAPI + Streamlit)

A Retrieval-Augmented Generation (RAG) application that allows users to upload a PDF and ask questions.
The system retrieves relevant content using FAISS + embeddings and generates answers using an LLM
(Gemini/OpenAI) with page-level citations to reduce hallucination.

---

## 🚀 Features
- Upload PDF and ask questions
- Semantic search using FAISS vector store
- Local embeddings using sentence-transformers
- LLM answer generation (Gemini/OpenAI)
- Page citations + chunk previews
- FastAPI backend with Swagger docs
- Streamlit frontend UI

---

## 🏗 Architecture
PDF Upload → Text Extraction → Chunking → Embeddings → FAISS Vector DB → Top-K Retrieval → LLM Answer + Citations

---

## 🛠 Tech Stack
- FastAPI, Uvicorn
- Streamlit
- LangChain
- FAISS
- sentence-transformers
- Gemini API / OpenAI API

---

## ⚙️ Setup

### 1) Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate

