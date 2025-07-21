# Dark Web Monitoring & Alert Tool – Full Build Guide

---

## 0. Prerequisites

* Python 3.11
* Internet connection (downloads mirror feeds; no Tor required)

---

## 1. Setup

```powershell
cd dark_monitor
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 2. CLI usage

```powershell
# Live watch every 30 min for email + domain keywords
python -m cli watch --keywords user@example.com,example.com --interval 30

# Manual search of stored posts
python -m cli search --keywords example.com
```

---

## 3. REST API

```powershell
uvicorn api.main:app --reload --port 8005
```

* Search: <http://localhost:8005/search?q=example.com,test>
* Alerts: <http://localhost:8005/alerts?limit=20>

---

## 4. How it works

1. Async crawler fetches RSS/HTML feeds listed in `monitorlib.crawler.FEEDS`.
2. Each item is hashed and stored in SQLite FTS5 DB (`data/dark.db`).
3. Keyword matches are logged to `matches` table and exposed via CLI/API.
4. Modify `FEEDS` to add more mirrors.

---

Happy monitoring! 🌑
