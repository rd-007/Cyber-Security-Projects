# Log Anomaly Detector – Full Build Guide

Follow these steps to train the model (if needed) and detect anomalies in any plain-text log file.

---

## 0. Prerequisites

* Python 3.11
* (Large logs only) ≥4 GB RAM recommended

---

## 1. Setup

```powershell
cd Log Anomaly Detector
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 2. CLI usage

```powershell
# Scan a log and print anomalies (threshold −0.2 by default)
python -m cli scan C:\logs\system.log

# Tweak aggressiveness (lower threshold → more anomalies)
python -m cli scan C:\logs\system.log --threshold -0.3
```

The table shows line number, IsolationForest score, and truncated content.

---

## 3. REST API

```powershell
uvicorn api.main:app --reload --port 8002
```

Swagger UI: <http://localhost:8002/docs>

Example:
```powershell
curl -X POST http://localhost:8002/scan -F "file=@C:/logs/system.log"
```

Returns JSON array with `{line, score, content}`.

---

## 4. Model persistence / retraining

* On first run, a TF-IDF + IsolationForest model is trained on the first 10 000 lines of the input log and saved to `anomlib/_model.pkl`.
* Subsequent scans load this model for speed and consistency.
* Delete the file to force a fresh model or pre-train on representative logs then copy the pickle file to share with teammates.

---

## 5. Next improvements

* Live-tail mode using `watchdog` to stream anomalies in real-time.
* Parsers for structured JSON logs → build per-field features.
* Export findings to CSV/ElasticSearch.

---

Happy debugging! 🔍
