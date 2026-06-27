# 🤖 AI Research Copilot

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![ChromaDB](https://img.shields.io/badge/ChromaDB-VectorDB-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

AI Research Copilot is an AI-powered PDF research assistant that helps users upload documents, extract content, split long text into chunks, and answer questions from PDF files.

## 🚀 Features

- Upload PDF documents
- Extract text from uploaded PDFs
- Split long documents into smaller chunks
- Ask questions from PDF content
- Generate relevant answers from document text
- Streamlit-based interactive interface

## 🧠 How It Works

## 🏗️ Architecture

```text
                +-------------------+
                |   Upload PDF      |
                +---------+---------+
                          |
                          v
                +-------------------+
                |  Extract Text     |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Smart Chunking    |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Vector Search     |
                | (ChromaDB)        |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Gemini AI         |
                +---------+---------+
                          |
                          v
                +-------------------+
                | Accurate Answer   |
                +-------------------+
```

## 📷 Application Preview

### 🏠 Home Screen
![Home](assets/homepage_AI.png)

### 📄 Upload PDF
![Upload](assets/uploadfiile_AI.png)

### 🤖 Generated Answer
![Answer](assets/generateanswer_AI.png)

### 🔄 Workflow
![Workflow](assets/workflow_AI.png)
