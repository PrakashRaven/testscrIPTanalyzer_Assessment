# Test Summary Document

## Problem statement & scope
Analyze Playwright test scripts for flaky patterns, duplication, maintainability, and security issues.
Inputs: `tests/` directory.
Outputs: `reports/issues_report.csv`, `reports/summary_table.md`.

## How GenAI was used
- Generated candidate edge-case tests and negative scenarios.
- Suggested refactors (e.g., replace `time.sleep` with explicit locator waits).
- Assisted in producing the initial rule set for the analyzer.

## Corrections made to AI outputs
- Replaced AI-suggested `time.sleep` with locator-based waits where appropriate.
- Removed suggestions that included hard-coded credentials; instead used configuration placeholders.
- Tightened vague expected outcomes (from "page loads" to "confirmation message appears").

## Coding and security considerations
- Avoid hard-coded secrets; use environment variables or test fixtures for credentials.
- Avoid generic exception catching; prefer specific exceptions.
- Mask PII in test data and artifacts.

## Top findings (sample)
1. `tests/test_checkout_flaky.py` — uses `time.sleep` (HIGH risk for flakiness).
2. `tests/test_profile_duplicated.py` — duplicated blocks across tests (maintainability).
3. `tests/test_edgecases.py` — no assertions (MEDIUM risk).

## Recommended action plan
- Prioritize fixing HIGH issues: replace hard waits, add proper assertions.
- Refactor duplicated blocks into helpers or page objects.
- Add analyzer to CI to prevent regressions.
