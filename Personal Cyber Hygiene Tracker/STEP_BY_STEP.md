# Personal Cyber Hygiene Tracker – Full Build Guide

---

## 0. Prerequisites

* Windows 10/11 with PowerShell
* Python 3.11
* Admin privileges (some checks query system services)

---

## 1. Setup

```powershell
cd hygiene_tracker
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 2. CLI usage

```powershell
# Run today’s hygiene check
python -m cli check

# View last 10 scores
python -m cli history --limit 10
```

---

## 3. REST API

```powershell
uvicorn api.main:app --reload --port 8004
```

* Current status: <http://localhost:8004/status>
* History: <http://localhost:8004/history?limit=30>

---

## 4. Data storage

Results save to `data/hygiene.db` (SQLite). Delete or back it up to reset history.

---

Happy hardening! 🛡️
