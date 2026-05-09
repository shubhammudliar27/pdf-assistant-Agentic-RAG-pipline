# 📄 PDF Assistant

A local, privacy-first CLI chatbot that lets you ask natural language questions about any PDF document. Built with [Agno](https://github.com/agno-agi/agno), Groq's blazing-fast LLaMA inference, and a local Qdrant vector store — no data ever leaves your machine.

---

## ✨ Features

- **Conversational Q&A** over any PDF — employee handbooks, contracts, research papers, manuals
- **Local vector store** via Qdrant (no cloud, no API costs for embeddings)
- **Fast inference** using Groq's hosted LLaMA 3.1 8B Instant
- **Semantic search** with `sentence-transformers` (`all-MiniLM-L6-v2`)
- **Clean CLI** powered by Typer + Rich

---

## 🏗️ Architecture

```
PDF File
   │
   ▼
[ingest.py] ──► SentenceTransformer Embedder ──► Local Qdrant Vector DB
                                                         │
                                                         ▼
                                         [assistant.py] ─► Agno Agent
                                                         │
                                                         ▼
                                                   Groq (LLaMA 3.1)
                                                         │
                                                         ▼
                                                  CLI Response
```

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/your-username/pdf-assistant.git
cd pdf-assistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` and add your [Groq API key](https://console.groq.com) (free tier available):

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Place your PDF in the `data/` folder

```bash
mkdir data
cp /path/to/your/document.pdf data/document.pdf
```

> **Note:** The `data/` folder is git-ignored to prevent accidental commits of sensitive documents.

### 6. Index your PDF (run once)

```bash
python src/ingest.py --pdf-path data/document.pdf
```

This chunks and embeds the PDF into a local Qdrant store at `./qdrant_storage/`. You only need to run this once per document.

### 7. Start chatting

```bash
python src/assistant.py
```

---

## 📁 Project Structure

```
pdf-assistant/
├── src/
│   ├── assistant.py      # Main CLI chatbot loop
│   └── ingest.py         # PDF indexing script (run once)
├── data/                 # Drop your PDFs here (git-ignored)
├── qdrant_storage/       # Auto-generated vector store (git-ignored)
├── .env.example          # Environment variable template
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `GROQ_API_KEY` | Your Groq API key | — |
| `PDF_PATH` | Default PDF path (used in assistant.py) | `data/document.pdf` |

To switch the LLM model, edit `src/assistant.py` and change the `id` field in the `Groq(...)` constructor. Available Groq models: `llama-3.1-8b-instant`, `llama-3.3-70b-versatile`, `mixtral-8x7b-32768`.

---

## 🧩 Tech Stack

| Component | Library |
|-----------|---------|
| Agent framework | [Agno](https://github.com/agno-agi/agno) |
| LLM inference | [Groq](https://groq.com) — LLaMA 3.1 8B |
| Embeddings | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Vector DB | [Qdrant](https://qdrant.tech) (local mode) |
| CLI | [Typer](https://typer.tiangolo.com) + [Rich](https://rich.readthedocs.io) |

---

## 🔒 Privacy

All embeddings and vector data are stored **locally** in `./qdrant_storage/`. The only external call is to Groq's inference API (your query + retrieved context chunks). Your PDF content is never sent to any third party for indexing.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License

MIT
