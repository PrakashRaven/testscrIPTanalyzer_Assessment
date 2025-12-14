# Manual Review Checklist

## Flaky patterns
- Hard-coded sleeps (time.sleep)
- Tests depending on order or shared global state
- Non-deterministic assertions (e.g., counts without conditions)

## Assertions
- Each test should have at least one meaningful assertion
- Negative tests should assert specific error messages or states

## Maintainability
- Common flows extracted to helpers/page objects
- Avoid copy-paste steps across tests
- Keep tests small and focused

## Security
- No hard-coded secrets
- Mask PII and avoid recording sensitive artifacts

## Error handling
- Do not catch generic Exception in tests
- Ensure teardown/cleanup logic runs reliably
