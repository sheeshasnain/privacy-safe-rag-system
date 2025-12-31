import re

PII_REGEX_PATTERNS = [
    r"\b\d{3}-\d{2}-\d{4}\b",          # SSN
    r"\b[A-Z]{2}\d{2}[A-Z0-9]{11,}\b", # IBAN
    r"\b\d{13,16}\b",                  # credit card
    r"\b\d{8,12}\b",                   # bank account
]

MAX_ALLOWED_CHARS = 2500       # hard safety ceiling
SUMMARY_THRESHOLD = 900        # when to shorten text


# ------------------------------
# 1️⃣ Therapy / hotline language cleaner
# ------------------------------
THERAPY_PHRASES = [
    "you're not alone",
    "grappling with difficult emotions",
    "courage to reach out",
    "mental health professional",
    "hotline",
    "reach out for support",
    "i want to offer you resources",
    "call",
    "crisis counselor",
    "emotional support"
]

def remove_therapy_language(text: str) -> str:
    lowered = text.lower()

    for phrase in THERAPY_PHRASES:
        if phrase in lowered:
            # Replace the entire answer with a neutral fallback
            return "I don't know."


    return text


# ------------------------------
# Existing helpers
# ------------------------------
def output_contains_pii(text: str) -> bool:
    for pattern in PII_REGEX_PATTERNS:
        if re.search(pattern, text):
            return True
    return False


def summarize(text: str, limit=400):
    text = text.strip()
    if len(text) <= limit:
        return text

    return text[:limit].rsplit(" ", 1)[0] + " …"


# ------------------------------
# Master validator
# ------------------------------
def validate_output(text: str):
    # A) remove therapy / counselor hallucinations first
    text = remove_therapy_language(text)

    # B) PII protection
    if output_contains_pii(text):
        return "❌ Response blocked due to sensitive data exposure."

    # C) Extremely long → trim hard
    if len(text) > MAX_ALLOWED_CHARS:
        short = summarize(text, limit=500)
        return f"(Shortened for safety)\n\n{short}"

    # D) Moderately long → gently shorten
    if len(text) > SUMMARY_THRESHOLD:
        short = summarize(text, limit=450)
        return f"(Here is a shorter version)\n\n{short}"

    # E) Otherwise return normally
    return text
