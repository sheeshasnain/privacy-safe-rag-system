import ollama

LABELS = [
    "normal",
    "educational",
    "self_harm",
    "fraud_or_theft",
    "hacking_misuse",
    "violence",
    "weapons_misuse",
    "privacy_invasion",
    "unknown"
]

PROMPT = """
You are a safety classifier.

Classify the user query into ONE of the categories below.

VERY IMPORTANT RULES:

• Questions about statistics, news, research, or general discussion ARE NOT unsafe.
• Suicide statistics or awareness questions are NOT self_harm.
• Only classify as self_harm if the user expresses intent, desire, or instructions related to harming themselves.
• Only classify as violence if the user wants to harm OTHER people.
• If unsure, choose "normal".

Categories:

normal
educational
self_harm
fraud_or_theft
hacking_misuse
violence
weapons_misuse
privacy_invasion
unknown

Return ONLY the label.

Query: "{text}"
"""


def classify_semantically(text: str) -> str:
    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {"role": "user", "content": PROMPT.format(text=text)}
        ],
        options={"temperature": 0}
    )

    label = response["message"]["content"].strip().lower()

    return label if label in LABELS else "unknown"
