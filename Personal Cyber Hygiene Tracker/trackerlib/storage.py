"""SQLite persistence for hygiene scores."""
from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import List, Tuple, Dict, Any
import datetime as dt

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "hygiene.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS history(
        ts TEXT PRIMARY KEY,
        score INTEGER,
        details TEXT
        )"""
    )
    return conn


def save_result(score: int, details: Dict[str, Any]):
    conn = _get_conn()
    conn.execute(
        "INSERT OR REPLACE INTO history(ts, score, details) VALUES(?,?,?)",
        (dt.datetime.utcnow().isoformat(), score, str(details)),
    )
    conn.commit()
    conn.close()


def fetch_history(limit: int = 30) -> List[Tuple[str, int]]:
    conn = _get_conn()
    cur = conn.execute(
        "SELECT ts, score FROM history ORDER BY ts DESC LIMIT ?", (limit,)
    )
    rows = cur.fetchall()
    conn.close()
    return rows
