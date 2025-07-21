# Practical & Modern Cybersecurity Projects (Python)

A curated collection of **six** end-to-end security tools – each fully offline, free, and ready to run on Windows (and most on macOS/Linux).  Every project ships with

* Clean Python 3.11 code
* Command-line interface (Typer + Rich)
* REST API (FastAPI + Uvicorn)
* Step-by-step usage guide (`STEP_BY_STEP.md` inside each folder)
* MIT Licence

| # | Project | Purpose |
|---|---------|---------|
| 1 | 🔗 **Real-Time Phishing URL Detector** | Real-time phishing URL classification (library + CLI + REST + browser extension) |
| 2 | 📡 **IoT Device Vulnerability Scanner** | Scans a subnet for IoT devices, fingerprints them, maps to offline CVE database |
| 3 | 📜 **AI-Based Log Anomaly Detector** | Isolation-Forest-based anomaly detector for plain-text logs |
| 4 | 🔒 **Privacy Risk Score Calculator for Apps** | Calculates a 0-100 privacy risk score from an app’s `AndroidManifest.xml` |
| 5 | 🛡️ **Personal Cyber Hygiene Tracker** | Checks local Windows hygiene (patch level, firewall, AV) & logs daily score |
| 6 | 🌑 **Dark Web Monitoring & Alert Tool** | Monitors clear-web mirrors of dark-web paste sites for keyword leaks |

---

## Quick Start (per project)

```powershell
# Example for project 1 – repeat per folder
cd phishing_detector
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Run REST API
uvicorn api.main:app --reload --port 8000
# OR use CLI
python -m cli --help
```
Open each project’s `STEP_BY_STEP.md` for detailed instructions, examples, Docker builds, and improvement ideas.



## Common Tech Stack

* Python 3.11  •  FastAPI  •  Typer & Rich  • SQLite / FTS5  • scikit-learn / IsolationForest  • APScheduler  • httpx  • psutil / WMI  • lxml

Each project declares its own `requirements.txt` to keep dependencies minimal.

---

## Contributing

Pull requests and issues are welcome!  For major changes, please open an issue first to discuss what you would like to change.

---

## Licence

[MIT](LICENSE)
