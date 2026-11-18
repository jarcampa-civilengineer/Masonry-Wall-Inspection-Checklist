from pathlib import Path
from datetime import datetime

def create_report(inspection):
    folder = Path("reports")
    folder.mkdir(exist_ok=True)
    safe_wall = "".join(c if c.isalnum() or c in "-_" else "_" for c in inspection["wall"])
    filename = folder / f"masonry_inspection_{safe_wall}_{datetime.now():%Y%m%d_%H%M%S}.txt"
    counts = {s: sum(r["status"] == s for r in inspection["results"]) for s in ("PASS","FAIL","N/A")}
    lines = [
        "MASONRY WALL INSPECTION REPORT", "=" * 34,
        f"Project: {inspection['project']}", f"Wall / Location: {inspection['wall']}",
        f"Inspector: {inspection['inspector']}", f"Date: {inspection['date']}", "",
        f"Summary: PASS {counts['PASS']} | FAIL {counts['FAIL']} | N/A {counts['N/A']}", "",
        "CHECKLIST DETAILS", "-" * 34
    ]
    for r in inspection["results"]:
        lines += [f"{r['id']} | {r['category']} | {r['status']}", r["description"],
                  f"Comments / corrective action: {r['notes'] or 'None recorded'}", ""]
    lines += ["Inspector signature: ______________________________",
              "Date: __________________",
              "", "This checklist is a documentation aid, not a substitute for approved",
              "drawings, specifications, applicable codes or the responsible design professional."]
    filename.write_text("\n".join(lines), encoding="utf-8")
    return filename
