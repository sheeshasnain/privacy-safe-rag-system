def refusal_message(intent: str) -> str:
    messages = {
        "self_harm": (
            "I’m really sorry you’re feeling this way. "
            "I can’t help with self-harm, but you deserve support. "
            "Please reach out to someone you trust or a local mental-health professional."
        ),
        "theft": (
            "I can’t help with stealing, fraud, or illegal shortcuts. "
            "If you'd like, I can explain legal and safe alternatives."
        ),
        "hack_misuse": (
            "I can’t help with breaking into accounts or systems. "
            "If you'd like, I can help with cybersecurity and staying safe instead."
        ),
        "violence": (
            "I can’t help with harming others. "
            "If you’re feeling angry, we can talk through safer ways to handle it."
        ),
        "weapons_misuse": (
            "I can’t help with instructions for using or building weapons to harm others. "
            "If you’re concerned about safety, I can share general safety information instead."
        ),

        "privacy_invasion": (
            "I can’t help with spying on someone, tracking them, or invading their privacy. "
            "If you want, I can explain legal and ethical ways to stay safe online instead."
        )        


    }

    return messages.get(intent, "I can’t help with that.")
