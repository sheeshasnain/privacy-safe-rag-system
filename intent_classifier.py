def classify_intent(query: str) -> str:
    text = query.lower()

# Allow statistics / informational questions about suicide
    if "suicide" in text and ("number" in text or "statistics" in text or "rate" in text):
        return "normal"

    SELF_HARM = [
        "kill myself",
        "end my life",
        "commit suicide",
        "how to die",
        "i want to die"
        ]
    if any(p in text for p in SELF_HARM):
        return "self_harm"


    # Theft / fraud intent
    THEFT = [
        "steal",
        "scam",
        "fraud",
        "clone card",
        "bypass payment",
        "rob"
    ]
    if any(p in text for p in THEFT):
        return "theft"

    # Hacking misuse intent
    HACK_MISUSE = [
        "hack wifi",
        "hack account",
        "exploit",
        "crack password",
        "bypass login"
    ]
    if any(p in text for p in HACK_MISUSE):
        return "hack_misuse"

    # Violence intent
    VIOLENCE = [
        "hurt someone",
        "attack someone",
        "kill someone",
        "beat someone"
    ]
    if any(p in text for p in VIOLENCE):
        return "violence"
    
    # Weapons misuse
    WEAPONS = [
        "how to use a gun to hurt",
        "how to stab someone",
        "how to shoot someone",
        "how to make a weapon",
        "how to attack with knife"
    ]
    if any(p in text for p in WEAPONS):
        return "weapons_misuse"
    
    # Privacy invasion
    PRIVACY = [
        "track someone secretly",
        "find someone's address",
        "spy on someone",
        "read someone's messages",
        "bypass someone's password"
    ]
    if any(p in text for p in PRIVACY):
        return "privacy_invasion"



    return "normal"
