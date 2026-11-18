# Masonry Wall Inspection Checklist

A lightweight command-line Python tool for recording masonry wall field inspections.

## Features
- Checklist organized by pre-installation, materials, layout, workmanship, reinforcement/grout, connections and final review.
- Records each item as PASS, FAIL or N/A.
- Captures comments and corrective-action notes.
- Appends inspection history to `inspection_history.csv`.
- Generates a timestamped text report in the `reports/` directory.

## Files
- `main.py` — interactive application.
- `checklist_data.py` — editable inspection items.
- `inspection_manager.py` — CSV record storage.
- `report_generator.py` — text report generation.
- `validators.py` — reusable date and status validation helpers.

## Requirements and execution
Python 3.8 or newer. No third-party packages are required.

```bash
python main.py
```

## Important
Customize the checklist for the approved project drawings, specifications, inspection
and testing plan, adopted building code, and applicable standards (such as the
project-referenced TMS/ACI requirements). Generic checklist prompts are not
acceptance criteria. Record actual measurements and specified tolerances in the
comments or add project-specific fields. Document failed items, corrective action,
responsible party and reinspection/closure.
