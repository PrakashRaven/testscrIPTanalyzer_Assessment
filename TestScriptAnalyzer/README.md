
# Full Python Playwright Project - Enhanced (Assessment Ready)

This enhanced package includes:
- Full Playwright tests (tests/)
- Analyzer (analyzer/)
- Documentation (docs/)
- GenAI prompts (genai/)
- CI workflow (.github/)
- Security notes, fix suggestions, reports, charts, Excel export

---

# 🚀 HOW TO RUN THE PROJECT

## 1️⃣ Activate Virtual Environment

### Windows (PowerShell)
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Windows (CMD)
```
python -m venv .venv
.venv\Scripts\activate.bat
```

### macOS / Linux
```
python3 -m venv .venv
source .venv/bin/activate
```

---

## 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

---

## 3️⃣ Install Playwright Browsers
```
python -m playwright install
```

---

## 4️⃣ Run Playwright Tests

### Run ALL tests:
```
pytest
```

### Run only smoke tests:
```
pytest -m smoke
```

### Run a single test file:
```
pytest tests/test_login.py
```

---

## 5️⃣ Run the Analyzer (Code Review Tool)

This scans for:
✔ flaky waits  
✔ duplication  
✔ missing assertions  
✔ generic exception handling  
✔ maintainability issues  

### Command:
```
python -m analyzer.main --input-dir tests --out-dir reports
```

Outputs:
- `reports/issues_report.csv`
- `reports/summary_table.md`
- `reports/summary_chart.png`
- `reports/summary_report.xlsx`

---

## 6️⃣ Run Fix Suggestions Script
```
python fix_suggestions/suggest_fixes.py tests/test_checkout_flaky.py
```

---

## 7️⃣ CI Workflow (GitHub Actions)

Located at:
```
.github/workflows/ci.yml
```

When pushed to GitHub, it will:
- Install dependencies  
- Run Playwright tests  
- Run analyzer  
- Upload reports  

---

Everything is fully ready for the assessment. 🚀
