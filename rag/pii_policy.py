FORBIDDEN_FIELDS = {
    "email",
    "phone",
    "address",
    "national_id",
    "bank_account_number",
    "iban",
    "credit_card_number",
    "credit_card_cvv",
    "salary",
    "medical_notes",
    "date_of_birth",
}

ALLOWED_FIELDS = {
    "name",          # only for anonymized reference
    "bank_name"      # allowed in aggregate
}
