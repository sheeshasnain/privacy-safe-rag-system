# =========================
# PROMPT INJECTION
# =========================
PROMPT_INJECTION_PATTERNS = [
    "ignore previous",
    "disregard instructions",
    "system prompt",
    "developer message",
    "act as",
    "jailbreak",
]

# =========================
# Explicit self-harm intent (block these)
# =========================
SELF_HARM_PHRASES = [
    "i want to kill myself",
    "i want to die",
    "i am going to commit suicide",
    "how to kill myself",
    "ways to die",
    "how can i end my life"
]

# =========================
# PII FIELD KEYWORDS
# =========================
PII_FIELDS = [
    "ssn", "national id", "account number",
    "iban", "bank account", "credit card",
    "cvv", "salary", "medical",
    "email", "phone", "address",
    "date of birth"
]
