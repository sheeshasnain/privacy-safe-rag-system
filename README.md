# 🔐 Privacy-Safe RAG System (Gemma 3, 1B)

This project is a **Privacy-Safe Retrieval Augmented Generation (RAG) system** designed to answer questions while protecting sensitive user data.

It combines:

✅ Local LLM: **Gemma 3 (1B)**  
✅ Retrieval from a local CSV dataset  
✅ Strong guardrails (privacy, safety, intent detection)  
✅ Hybrid routing: **LLM mode + RAG mode** depending on the question  

The system is able to:

- Answer questions about bank data from the dataset (RAG mode)
- Refuse unsafe or malicious queries
- Prevent exposure of names, account numbers, phone numbers, etc.
- Allow harmless statistical queries (like suicide statistics, crime rate, etc.)
- Say *“I don’t know”* when the dataset doesn’t contain the answer

---

## 🧠 How It Works

### 1️⃣ Query Classifier
Determines whether a user question is:

- normal
- self-harm intent
- violence
- hacking
- fraud
- privacy invasion
- informational statistics (allowed)

### 2️⃣ Hybrid Routing

| Query Type | What Happens |
|----------|--------------|
| Dataset related (banks, customers, accounts) | → RAG mode (sanitized context) |
| General questions | → LLM mode |
| Dangerous / private data requests | → Blocked politely |

---

## 🏗 Architecture Overview

```text
User Query
│
▼
Input Guardrails (intent + semantic + PII filter)
│
├── blocked → refuse safely
│
└── allowed
    │
    ├── dataset question → RAG pipeline
    └── general question → LLM

```

## ▶️ Running the Project

1. Install **Ollama**
   https://ollama.com

2. Pull Gemma:
    ollama pull gemma3:1b

3. Install Python dependencies:
    pip install pandas
4. Run the project:
    python -m rag.run_rag

📂 Dataset
The demo dataset is synthetic and contains anonymized customers such as:

bank name

branch

gender

age group

Sensitive items like:

phone

address

IBAN

credit card

national ID

are protected by the guardrails and never exposed.

🔒 Safety & Guardrails
The system blocks:

❌ Self-harm instructions
❌ Violence or weapon misuse
❌ Hacking or cyber-crime
❌ Fraud / stealing money
❌ Accessing personal records or accounts
❌ Prompt injections

But allows:

✅ Research statistics
✅ Educational questions
✅ Bank dataset exploration (RAG only)

⭐ Why This Project Matters
This project demonstrates how AI systems should:

✔ respect privacy
✔ avoid hallucinating facts
✔ explain safely
✔ avoid unnecessary censorship
✔ and stay useful

Perfect for:

university submission

AI portfolio

interview demo

GitHub profile

🙌 Author
Built by M.SHEES HASNAIN (AI/ML Engineer)
Focus areas: LLMs • RAG • Guardrails • Applied AI

📌 Contributions / Improvements Ideas
Future upgrades:

web retrieval

Docker support

frontend UI