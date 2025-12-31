from .pii_policy import ALLOWED_FIELDS, FORBIDDEN_FIELDS

def sanitize_record(record):
    return { 
        k: v for k, v in record.items()
        if k not in FORBIDDEN_FIELDS
    }

def retrieve_safe_context(records, limit=10):
    safe_records = []
    for r in records[:limit]:
        r_copy = {k: v for k, v in r.items() if k not in FORBIDDEN_FIELDS and k != "name"}
        safe_records.append(r_copy)
    return safe_records
def format_context(records):
    formatted = []
    for r in records:
        # Only keep allowed fields
        allowed_info = {k: v for k, v in r.items() if k in ALLOWED_FIELDS}
        if allowed_info:
            formatted.append(", ".join(f"{k}: {v}" for k, v in allowed_info.items()))
    return "\n".join(formatted)



