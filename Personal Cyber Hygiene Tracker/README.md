# Personal Cyber Hygiene Tracker

Runs local checks on a Windows machine to compute a daily security hygiene score and stores historical results.

Components:
1. `trackerlib` – individual system checks, scoring, SQLite history
2. CLI – one-shot check & history view
3. REST API – FastAPI service exposing current status and history

All logic executes locally; no data leaves the machine.
