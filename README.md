<div align="center">

# 🏦 Enterprise Risk RAG
### AI-Powered Regulatory Knowledge Assistant

**Retrieval-Augmented Generation (RAG) for Banking & Financial Regulations**

Basel III • IFRS • RBI • LangChain • FAISS • Sentence Transformers • Groq • Streamlit

### 🌐 Live Demo

[![Live Demo](https://img.shields.io/badge/🚀%20Launch%20App-Live-success?style=for-the-badge)](https://enterprise-risk-rag-kss7m8mpjken3stwbxzmeq.streamlit.app/)



![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green?style=for-the-badge)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)
[![Status](https://img.shields.io/badge/Status-Work in Progress-yellow.svg)]()


</div>

---

# 📌 Overview

Enterprise Regulatory RAG is a production-style Retrieval-Augmented Generation (RAG) application designed for **banking and financial regulatory intelligence**.

Instead of relying solely on an LLM, the system retrieves relevant regulatory context from **Basel III**, **IFRS** and **RBI** documents before generating grounded, citation-backed responses.

---

# ✨ Features

- 📄 Multi-document regulatory knowledge base
- 🔍 Semantic search using Sentence Transformers
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ FAISS Vector Database
- 🤖 Groq LLM Integration
- 📚 Citation-grounded responses
- 📑 Source page attribution
- 🎯 Prompt engineering to reduce hallucinations
- 🌐 Interactive Streamlit interface
- 🏗️ Modular production-ready codebase

---

## 📚 Regulatory Corpus

### Current
- ✅ Basel III

### Planned
- 🔄 IFRS
- 🔄 RBI Master Circulars & Guidelines

---

# ⚙️ Tech Stack

| Layer | Technology |
|--------|------------|
| Language | Python |
| Framework | LangChain |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| LLM | Groq (Llama 3.3 70B) |
| Frontend | Streamlit |
| Document Loader | PyPDF |
| Prompting | Prompt Templates |
| Retrieval | Similarity Search |
| Version Control | Git & GitHub |

---

# 🧠 RAG Pipeline

```text
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Chunking
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Retrieval
      │
      ▼
Prompt Construction
      │
      ▼
Groq LLM
      │
      ▼
Grounded Response + Citations
```

---

# 📂 Project Structure

```text
Enterprise-Risk-RAG/
│
├── app.py
├── requirements.txt
├── README.md
│
├── src/
│   ├── data_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   └── rag_pipeline.py
│
├── notebooks/
│   ├── 01_data_loader.ipynb
│   ├── 02_text_chunking.ipynb
│   ├── 03_embeddings.ipynb
│   ├── 04_vector_database.ipynb
│   ├── 05_retrieval.ipynb
│   └── 06_llm_generation.ipynb
│
├── vectorstore/
│   └── faiss_index/
│
└── data/
```

---

# 🚀 Installation

```bash
git clone https://github.com/<username>/Enterprise-Risk-RAG.git

cd Enterprise-Risk-RAG

pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=your_api_key
```

---

# ▶️ Run

```bash
streamlit run app.py
```

---

# 💬 Example Questions

- What is Common Equity Tier 1?
- Explain Liquidity Coverage Ratio.
- What are Pillar 3 disclosure requirements?
- What is the Net Stable Funding Ratio?
- Explain Expected Credit Loss under IFRS 9.
- What are RBI provisioning norms?

---

# 🎯 Key Capabilities

✅ Retrieval-Augmented Generation

✅ Semantic Search

✅ Vector Embeddings

✅ FAISS Indexing

✅ Citation Grounding

✅ Prompt Engineering

<!-- ✅ Hallucination Reduction -->

✅ Production-style Modular Architecture

---

# 📈 Future Enhancements

- Multi-Document QA
- Conversation Memory
- Regulatory Change Monitoring
- Evaluation Framework
- Docker Deployment
- Cloud Deployment (AWS/GCP/Azure)

---

# 👩‍💻 Author

**Shrabani Das**

Data Scientist | Credit Risk Analytics | LLM & RAG | Financial AI

---

<div align="center">

### ⭐ If you found this project useful, consider starring the repository.

</div>