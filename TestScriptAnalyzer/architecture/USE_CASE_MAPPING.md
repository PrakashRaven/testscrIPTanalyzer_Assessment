
# Use Case Mapping

| Requirement | Implementation |
|------------|----------------|
| Flaky waits detection | rules.yml → FLAKY_HARD_WAIT + scanner.py |
| Duplicate code detection | duplication.py |
| Analyzer output | reporting.py → CSV, MD, PNG, XLSX |
| GenAI usage | genai/prompts_and_outputs.md |
| Documentation | docs/ folder |
| CI integration | .github/workflows/ci.yml |
| Negative/edge test scenarios | tests/ folder |
