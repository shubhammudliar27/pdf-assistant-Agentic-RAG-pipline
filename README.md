# 📄 PDF Assistant — Ask Questions to Any Document

Ever wished you could just *ask* a document a question instead of reading through 50 pages to find one answer?

That's exactly what this does.

**PDF Assistant** is a simple chat tool that lets you have a conversation with any PDF file — like an employee handbook, a contract, a research paper, or a policy document. You type your question, and it finds the answer from the document in seconds.

---

## 🙋 What Can It Do?

Here are some real examples of the kinds of questions you can ask:

> *"How many days of annual leave am I entitled to?"*

> *"What is the company's work from home policy?"*

> *"What happens if I want to resign? What's the notice period?"*

> *"Is there a policy on reimbursements?"*

> *"What are the rules around confidentiality?"*

Instead of scrolling through the document yourself, you just ask — and it gives you a direct, accurate answer with the relevant information pulled from the document.

---

## 💡 How Is This Different From Just Searching a PDF?

| Regular PDF Search | PDF Assistant |
|---|---|
| You search for a keyword | You ask a full question in plain English |
| You get a page number | You get a direct answer |
| You have to read and interpret | It reads and interprets for you |
| One keyword at a time | Understands context and meaning |

Think of it like having a smart assistant who has read the entire document and is ready to answer anything you ask about it.

---

## 🔒 Your Data Stays Private

This tool runs **entirely on your computer**. Your documents are never uploaded to any server or stored in the cloud. The only external connection is to process your question through an AI model — your actual document content stays local.

This makes it safe to use with sensitive internal documents like HR policies, legal contracts, or financial reports.

---

## 🛠️ Setup Guide

> If someone else is setting this up for you, just share this README with them.

### What You Need Before Starting

- Python 3.9 or higher installed on your computer
- A free [Groq API key](https://console.groq.com) (takes 2 minutes to create)
- Your PDF file

### Setup Steps

**1. Clone the repository**
```bash
git clone https://github.com/your-username/pdf-assistant.git
cd pdf-assistant
```

**2. Create a virtual environment**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**
```bash
cp .env.example .env
```
Open `.env` and paste your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

**5. Place your PDF in the `data/` folder**
```bash
mkdir data
cp /path/to/your/document.pdf data/document.pdf
```

**6. Index the PDF — run this once**
```bash
python src/ingest.py --pdf-path data/document.pdf
```
This reads and processes the document so the assistant can search through it. You only need to do this once per document.

**7. Start chatting**
```bash
python src/assistant.py
```

---

## 📁 Project Structure

```
pdf-assistant/
├── src/
│   ├── assistant.py      # The chat interface
│   └── ingest.py         # Reads and indexes the PDF (run once)
├── data/                 # Place your PDF files here (not uploaded to GitHub)
├── qdrant_storage/       # Where the indexed document is stored locally
├── .env.example          # Template for your API key
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| What It Does | Tool Used |
|---|---|
| Understanding your questions | Groq — LLaMA 3.1 8B (AI model) |
| Reading & searching the PDF | Sentence Transformers + Qdrant |
| Connecting everything together | Agno Agent Framework |
| The chat interface | Typer + Rich |

---

## 🔄 Want to Use a Different Document?

Just run the ingest step again with your new PDF:
```bash
python src/ingest.py --pdf-path data/new-document.pdf
```

---

## 📄 License

MIT — free to use, modify, and share.
