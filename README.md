# Headercheck

A small Python CLI tool that fetches a URL and reports the presence
and values of three HTTP security headers:

- X-Content-Type-Options
- Content-Security-Policy
- Strict-Transport-Security

## Installation

Requirements: Python 3 with pip and venv support.

From the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

```bash
python headercheck.py
```

Enter a complete URL, including http:// or https://.

## Limitations

- Checks header presence, not whether its configuration is secure.
- A missing header does not automatically mean a vulnerability.
- Follows redirects and examines the final response.
- HSTS is only effective when received over HTTPS.
- This is a learning project, not a complete security scanner.

# headercheck
Python CLI tool for inspecting HTTP security headers
