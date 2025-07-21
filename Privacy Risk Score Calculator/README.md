# Privacy Risk Score Calculator for Apps

Calculates a numeric privacy-risk score for mobile/desktop apps based on their declared permissions.

Components:
1. `scorlib` – manifest parsing, weighting logic, score computation.
2. CLI – quick scoring from the terminal.
3. REST API – FastAPI endpoint.

Runs fully offline using local YAML weight profiles.
