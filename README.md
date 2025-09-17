# Intentionally Insecure Python Examples (For Education Only)

⚠️ **WARNING**: This repository contains code that is intentionally **unsafe**, **outdated**, and **badly designed** for training purposes.
**Do NOT** deploy, run in production, or copy-paste into real projects. Use only in isolated, disposable environments.

## What this repo demonstrates
- Hard‑coded secrets and credentials
- Use of outdated/vulnerable library versions
- SQL injection and command injection
- Insecure deserialization
- Weak cryptography and poor randomness
- Insecure HTTP usage (disabling TLS verification)
- Logging sensitive data
- Unsafe YAML loading

## Structure
- `app_insecure_flask.py` — Flask app with multiple issues (debug, hardcoded secret, SQLi, etc.)
- `hardcoded_secret.py` — Demonstrates embedding a fake secret in code.
- `insecure_requests.py` — Disables TLS verification, uses HTTP, embeds credentials in URL.
- `outdated_crypto.py` — Uses MD5 and predictable randomness.
- `unsafe_deserialization.py` — Uses `pickle.loads` on untrusted input.
- `command_injection.py` — Shells out with unsanitized user input.
- `yaml_load.py` — Uses `yaml.load` without a safe loader.
- `logging_sensitive.py` — Logs plaintext passwords and tokens.
- `requirements.txt` — Pinning intentionally outdated versions.

## Ethics & Usage
- All secrets are **fake** placeholders.
- Purpose is to help learners identify, test, and fix insecure patterns.
- Pair with linters/scanners (e.g., Bandit, Semgrep, trufflehog) to practice detection.
- Consider exercises:
  - Identify vulnerabilities and write patches.
  - Add tests that assert secure behavior.
  - Upgrade dependencies and fix breaking changes safely.

## Getting started (in a sandbox only)
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# Run a single file as needed, e.g.:
python app_insecure_flask.py
```

## License
MIT — provided as-is, without any warranty. Educational use only.