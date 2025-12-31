import ollama
from input_guardrails import validate_user_input
from output_guardrails import validate_output

SYSTEM_PROMPT = """
You are a concise assistant.

Rules:
- Keep answers under 4–5 sentences.
- No unnecessary disclaimers unless the user explicitly asks medical questions.
- Be clear, direct, and simple.
"""


def safe_chat(user_input: str):
    allowed, error = validate_user_input(user_input)
    if not allowed:
        return error

    response = ollama.chat(
    model="gemma3:1b",
    messages=[ ... ],
    options={
        "temperature": 0.4,
        "num_predict": 120    # limits length
    }
)


    raw_output = response["message"]["content"]
    return validate_output(raw_output)
