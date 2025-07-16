# Real-Time Phishing URL Detector

A fully offline, Python-based toolkit that detects phishing URLs. It exposes:

1. **Library (`phishlib`)** – reusable feature extraction + ML model
2. **CLI** – quick scans from the terminal
3. **REST API (FastAPI)** – JSON endpoint for programmatic access
4. **Browser extension** – Manifest v3 add-on that queries your local API

---

## Quick start
```bash
# install deps
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# run REST API
uvicorn api.main:app --reload  # http://localhost:8000/docs

# run single-URL scan via CLI
python -m cli scan https://example.com
```

## Project structure
```
phishing_detector/
  phishlib/      core code (features, model, utils)
  api/           FastAPI app
  cli/           Typer CLI wrapper
  extension/     browser extension (manifest v3)
  data/          datasets + training script
  tests/         pytest unit tests
```
