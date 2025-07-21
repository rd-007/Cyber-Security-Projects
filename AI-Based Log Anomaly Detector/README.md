# AI-Based Log Anomaly Detector

Offline tool that flags unusual log entries using an unsupervised IsolationForest model.

Components
1. `anomlib` – parsing, vectorisation, model
2. CLI – one-shot or streaming scan
3. REST API – FastAPI

Runs fully locally with no external dependencies beyond free Python packages.
