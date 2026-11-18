from checklist_data import CHECKLIST
from inspection_manager import save_inspection
from report_generator import create_report

def main():
    print("\nMASONRY WALL INSPECTION CHECKLIST")
    info = {
        "project": input("Project name: ").strip() or "Not specified",
        "wall": input("Wall / location ID: ").strip() or "Not specified",
        "inspector": input("Inspector: ").strip() or "Not specified",
        "date": input("Date (YYYY-MM-DD): ").strip() or "Not specified",
    }
    results = []
    for item in CHECKLIST:
        print(f"\n{item['id']} | {item['category']}\n{item['description']}")
        while True:
            status = input("Result [P=Pass, F=Fail, N=N/A]: ").strip().upper()
            if status in ("P", "F", "N"):
                break
            print("Enter P, F, or N.")
        note = input("Comments / corrective action: ").strip()
        results.append({**item, "status": {"P":"PASS","F":"FAIL","N":"N/A"}[status], "notes": note})
    inspection = {**info, "results": results}
    save_inspection(inspection)
    report = create_report(inspection)
    print(f"\nSaved inspection history. Report: {report}")
    print("Summary:", " | ".join(f"{s}: {sum(r['status']==s for r in results)}" for s in ("PASS","FAIL","N/A")))

if __name__ == "__main__":
    main()
