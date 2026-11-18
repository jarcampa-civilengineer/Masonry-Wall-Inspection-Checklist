import csv
from pathlib import Path

def save_inspection(inspection, filename="inspection_history.csv"):
    path = Path(filename)
    exists = path.exists()
    fields = ["project","wall","inspector","date","id","category","description","status","notes"]
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if not exists:
            writer.writeheader()
        for item in inspection["results"]:
            writer.writerow({**{k: inspection[k] for k in ("project","wall","inspector","date")}, **item})
    return path
