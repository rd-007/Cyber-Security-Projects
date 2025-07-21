# Privacy Risk Score Calculator – Full Build Guide

---

## 0. Prerequisites

* Python 3.11

---

## 1. Setup

```powershell
cd Privacy Risk Score Calculator 
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## 2. CLI usage

```powershell
# Score an AndroidManifest.xml
python -m cli score C:\apps\AndroidManifest.xml
```

Output: Rich table of risky permissions + overall 0–100 score.

---

## 3. REST API

```powershell
uvicorn api.main:app --reload --port 8003
```

Swagger UI: http://localhost:8003/docs

Example:
```powershell
curl -X POST http://localhost:8003/score -F "manifest=@C:/apps/AndroidManifest.xml"
```

---

## 4. Custom weight profiles

Edit `data/weights_default.yaml` or create a new YAML file and pass its path to `load_weights()` in a small wrapper script.

---

Happy auditing! 🔒
