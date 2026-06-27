# 🤖 AI Research Copilot

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

### Home Screen

![Home](C:\Users\navul\OneDrive\Desktop\kesika\full time\AIML\homepage_AI.png)

### Upload PDF

![Upload](images/upload.png)

### Generated Answer

![Answer](images/answer.png)
