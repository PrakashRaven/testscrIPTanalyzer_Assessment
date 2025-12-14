# Code Review Analytics Summary

## Issues by File and Severity

| File | HIGH | MEDIUM | LOW | Total |
|------|------|--------|-----|-------|
| `tests\test_checkout_flaky.py` | 2 | 1 | 0 | 3 |
| `tests\test_edgecases.py` | 0 | 1 | 0 | 1 |
| `tests\test_login.py` | 0 | 1 | 0 | 1 |
| `tests\test_profile_duplicated.py` | 1 | 2 | 0 | 3 |

## Duplicate Blocks

- Duplicate block `4a812e66` appears in:
  - `tests\test_profile_duplicated.py` at ~line 9
  - `tests\test_profile_duplicated.py` at ~line 17
```text
_common_steps(page)
page.goto("https://demo.playwright.dev/todomvc")
page.locator("input.new-todo").fill("Profile step")
page.locator("input.new-todo").press("Enter")
```

- Duplicate block `2c8b1dfa` appears in:
  - `tests\test_profile_duplicated.py` at ~line 10
  - `tests\test_profile_duplicated.py` at ~line 18
```text
page.goto("https://demo.playwright.dev/todomvc")
page.locator("input.new-todo").fill("Profile step")
page.locator("input.new-todo").press("Enter")
assert page.locator("ul.todo-list li").count() >= 1
```

