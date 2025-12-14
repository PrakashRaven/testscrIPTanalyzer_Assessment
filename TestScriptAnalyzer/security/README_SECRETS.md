# Security: Secrets & Test Data Guidelines

- Never store production credentials in test code or repository.
- Use environment variables or a secrets manager for credentials.
- Provide a `.env.example` with placeholders (do not commit real secrets).
- Mask PII in logs and test artifacts before sharing.
