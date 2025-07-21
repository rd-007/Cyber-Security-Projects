# Dark Web Monitoring & Alert Tool

Monitors selected dark-web paste sites (via clear-web mirrors) for user-defined keywords and raises local alerts.

Components:
1. `monitorlib` – async crawler, SQLite FTS5 storage, keyword search
2. CLI – live watch & manual search
3. REST API – FastAPI endpoints for subscription and alert retrieval

No external paid APIs; all data stored locally.
