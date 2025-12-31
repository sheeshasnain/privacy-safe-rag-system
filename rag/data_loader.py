import csv

def load_dataset(path="synthetic_sensitive_users.csv"):
    records = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records
