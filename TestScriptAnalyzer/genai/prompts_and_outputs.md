# GenAI Prompts and Sample Outputs

## Prompt: Generate edge cases for bank transfer feature
> You are a senior QA engineer. Application: online banking. Feature: internal transfers.
> Generate 10 positive, 10 negative, and 5 edge cases with preconditions, steps, expected results.

### Sample (edge case)
- Concurrent transfers: Two transfers executed at the same time from same account. Expected: system avoids double-spend and ensures accurate balances.

## Prompt: Review flaky Selenium test
> Paste test code and ask the model to identify flakiness and suggest fixes.

### Sample AI suggestion (validated and edited)
- Replace `time.sleep(5)` with `WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'selector')))`
- Use page object locators to avoid brittle selectors
