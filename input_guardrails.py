from intent_classifier import classify_intent
from semantic_classifier import classify_semantically
from refusal_messages import refusal_message

# Trigger words that require semantic checking
TRIGGER_WORDS = [
    "bank", "account", "credit card", "iban"
]

# Medical blocklist (unchanged)
MEDICAL_BLOCKED = [
    "medical record",
    "diagnosis of",
    "patient history",
    "prescription for",
    "lab report",
    "medical file"
]

# Prompt injection patterns (unchanged)
from security_rules import PROMPT_INJECTION_PATTERNS
def contains_pattern(text, patterns):
    text = text.lower()
    return any(p in text for p in patterns)


def validate_user_input(user_input: str):
    text = user_input.lower()

    # ------------------------------
    # Step 1: Intent-based filtering
    # ------------------------------
    intent = classify_intent(user_input)
    if intent != "normal":
        return False, refusal_message(intent)

    # ------------------------------
    # Step 2: Semantic check for trigger words
    # ------------------------------
    if any(word in text for word in TRIGGER_WORDS):
        semantic_label = classify_semantically(user_input)
        # Block only unsafe semantic categories
        if semantic_label in ["self_harm", "privacy_invasion", "fraud_or_theft",
                              "violence", "weapons_misuse"]:
            return False, refusal_message(semantic_label)
        # Safe semantic categories like 'normal' or 'educational' → allow

    # ------------------------------
    # Step 3: Other guardrails
    # ------------------------------
    # Medical records
    if any(p in text for p in MEDICAL_BLOCKED):
        return False, "❌ Access to personal medical records is forbidden."

    # Prompt injection
    if contains_pattern(text, PROMPT_INJECTION_PATTERNS):
        return False, "❌ Prompt injection detected."

    return True, None
