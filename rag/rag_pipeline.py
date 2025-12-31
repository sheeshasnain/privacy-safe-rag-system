import ollama

from rag.data_loader import load_dataset
from rag.safe_retriever import retrieve_safe_context, format_context

from input_guardrails import validate_user_input
from output_guardrails import validate_output
from semantic_classifier import classify_semantically


SYSTEM_PROMPT = """
You are a concise factual assistant.

Rules:
• Answer questions directly and briefly.
• Suicide statistics, research, or awareness questions are allowed.
• Do NOT assume distress unless stated.
• Do NOT provide hotlines or therapy language unless asked.
• Do NOT refuse informational questions.
• If unsure, say: "I don't know."
• Never invent facts or numbers.

Privacy:
- Do NOT reveal personal identifying data.
- Only summarize what is relevant.
"""


# ---------------------------------------------------------
# Detect dataset-related keywords (RISK SIGNAL, not decision)
# ---------------------------------------------------------
def is_dataset_question(query: str) -> bool:
    q = query.lower()
    DATA_WORDS = [
        "dataset", "record", "customer", "account",
        "bank", "hbl", "ubl", "meezan",
        "list", "details", "data"
    ]
    return any(w in q for w in DATA_WORDS)


# ---------------------------------------------------------
# Main chat handler (Semantic-first Hybrid RAG)
# ---------------------------------------------------------
def rag_chat(user_query: str):

    # 1️⃣ Input guardrails
    allowed, error = validate_user_input(user_query)
    if not allowed:
        return error

    # 2️⃣ Semantic classification (CORE FIX)
    semantic = classify_semantically(user_query)

    # Only these semantics are allowed to touch dataset
    DATASET_ALLOWED_SEMANTICS = {
        "privacy_invasion",
        "unknown"
    }

    # -----------------------------------------------------
    # NORMAL MODE (default)
    # -----------------------------------------------------
    if not (is_dataset_question(user_query) and semantic in DATASET_ALLOWED_SEMANTICS):
        response = ollama.chat(
            model="gemma3:1b",
            messages=[
                {
                    "role": "system",
                    "content": "Answer briefly, clearly, and do not hallucinate."
                },
                {"role": "user", "content": user_query}
            ],
            options={"temperature": 0.4}
        )

        raw = response["message"]["content"]
        return validate_output(raw)

    # -----------------------------------------------------
    # RAG MODE (dataset-safe)
    # -----------------------------------------------------
    records = load_dataset()
    safe_records = retrieve_safe_context(records)
    context = format_context(safe_records)

    prompt = f"""
Answer factually in two or three sentences, or say "I don't know."

Rules:
- Do NOT reveal personal data.
- Do NOT list names or identifiers unless explicitly allowed.
- Do NOT mention datasets or internal sources.

Information:
{context}

Question:
{user_query}
"""

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        options={"temperature": 0.3}
    )

    raw = response["message"]["content"]
    return validate_output(raw)
