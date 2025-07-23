# ChatPDF + Summarizer 🔍📄 (Offline with Ollama)

This project lets you upload any PDF, extract text, summarize it using **local LLMs (like Gemma or LLaMA3 via Ollama)**, and ask custom questions — all without needing an OpenAI API key.

> ⚡ Fully offline & private. Powered by [Ollama](https://ollama.com).

---

## 🧰 Features

- 📁 Upload any PDF
- 🧠 Summarize using **offline models** (Gemma, LLaMA3, Mistral)
- ❓ Ask questions about the content
- 💾 Downloadable summary
- Built using `Streamlit`, `PyMuPDF`, and `Ollama`

---

## 🚀 How to Run

### 1. Prerequisites
- Python 3.8+
- Ollama installed and running
  - [Download Ollama](https://ollama.com/download)
  - Run a model:  
    ```bash
    ollama run gemma:2b
    ```

### 2. Install Python packages
```bash
pip install -r requirements.txt
