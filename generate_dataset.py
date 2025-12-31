from faker import Faker
import csv
import random

fake = Faker()

BANKS = [
    "HBL", "UBL", "ABL", "AL_Falah Bank",
    "Standard Chartered", "Meezan", "Bank AlHabib"
]

with open("synthetic_sensitive_users.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow([
        "name",
        "email",
        "phone",
        "address",
        "date_of_birth",
        "national_id",
        "bank_name",
        "bank_account_number",
        "iban",
        "credit_card_number",
        "credit_card_cvv",
        "salary",
        "medical_notes"
    ])

    for _ in range(100):
        writer.writerow([
            fake.name(),
            fake.email(),
            fake.phone_number(),
            fake.address().replace("\n", " "),
            fake.date_of_birth(minimum_age=18, maximum_age=70),
            fake.ssn(),
            random.choice(BANKS),
            fake.bban(),
            fake.iban(),
            fake.credit_card_number(),
            fake.credit_card_security_code(),
            fake.random_int(min=30000, max=150000),
            fake.sentence(nb_words=10)
        ])
