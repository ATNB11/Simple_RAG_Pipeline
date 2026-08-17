# 🧠 Simple RAG Pipeline with Qdrant

> A modular Retrieval-Augmented Generation (RAG) pipeline built with **Python**, **Qdrant**, **Sentence Transformers**, and **Cross-Encoder reranking**.

This project demonstrates how semantic search works end-to-end: documents are loaded, split into chunks, converted into vector embeddings, stored in a Qdrant vector database, and retrieved based on meaning rather than keywords. The retrieved results are then reranked to improve relevance before being returned to the user.

---

## ✨ Features

* 📄 Load and preprocess text documents
* ✂️ Chunk long documents into smaller passages
* 🔢 Generate **384-dimensional embeddings** with `all-MiniLM-L6-v2`
* 🗄️ Store vectors in a persistent **Qdrant** database
* 🔍 Perform semantic search using cosine similarity
* 🎯 Improve retrieval quality with **MS MARCO Cross-Encoder** reranking
* 💬 Interactive command-line interface
* 🧩 Clean and modular project structure

---

## 🏗️ RAG Workflow

```text
            Document (HR Policy)
                    │
                    ▼
            Load & Chunk Text
                    │
                    ▼
     all-MiniLM-L6-v2 Embeddings
                    │
                    ▼
        Qdrant Vector Database
                    │
                    ▼
        Semantic Vector Retrieval
                    │
                    ▼
   Cross-Encoder Relevance Reranking
                    │
                    ▼
       Top Relevant Context Chunks
```

---

## 📁 Project Structure

```text
.
├── data/
│   └── HR.txt              # Sample HR policy document
├── loader.py               # Document loading & chunking
├── embed.py                # Embedding generation
├── vectorDB.py             # Qdrant initialization & indexing
├── retrive.py              # Vector retrieval
├── reranker.py             # Cross-encoder reranking
├── main.py                 # CLI entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/simple-rag-qdrant.git
cd simple-rag-qdrant

python -m venv rag
source rag/bin/activate      # Linux / macOS
# rag\Scripts\activate       # Windows

pip install -r requirements.txt
```

---

## 🚀 Usage

Run the application:

```bash
python main.py
```

Example:

```text
Type your query...
> How many casual leaves do employees get?

Employees are entitled to 12 casual leave days per year.
```

---

## 🛠️ Tech Stack

| Component             | Technology                               |
| --------------------- | ---------------------------------------- |
| **Language**          | Python                                   |
| **Vector Database**   | Qdrant                                   |
| **Embeddings**        | `sentence-transformers/all-MiniLM-L6-v2` |
| **Reranker**          | `cross-encoder/ms-marco-MiniLM-L-6-v2`   |
| **Similarity Metric** | Cosine Distance                          |

---

## 📄 License

Released under the **MIT License**. Feel free to use and modify this project for learning and experimentation.
