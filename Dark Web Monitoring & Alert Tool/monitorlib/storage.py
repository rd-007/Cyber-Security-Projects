"""SQLite FTS5 storage and search."""
from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import List, Tuple, Dict, Any
import datetime as dt

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "dark.db"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def _get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys=ON;")
    conn.execute(
        """CREATE TABLE IF NOT EXISTS posts(
        id TEXT PRIMARY KEY,
        title TEXT,
        url TEXT,
        content TEXT,
        ts TEXT
        );"""
    )
    conn.execute(
        """CREATE VIRTUAL TABLE IF NOT EXISTS posts_fts USING fts5(content, content='posts', content_rowid='rowid');"""
    )
    conn.execute(
        """CREATE TABLE IF NOT EXISTS matches(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id TEXT,
        keyword TEXT,
        ts TEXT
        );"""
    )
    return conn


def init_db():
    _get_conn().close()


def store_post(post_id: str, title: str, url: str, content: str):
    ts = dt.datetime.utcnow().isoformat()
    conn = _get_conn()
    try:
        conn.execute(
            "INSERT OR IGNORE INTO posts(id, title, url, content, ts) VALUES(?,?,?,?,?)",
            (post_id, title, url, content, ts),
        )
        conn.execute(
            "INSERT INTO posts_fts(rowid, content) SELECT rowid, content FROM posts WHERE id=?",
            (post_id,),
        )
        conn.commit()
    finally:
        conn.close()


def search_keywords(keywords: List[str]) -> List[Dict[str, Any]]:
    pattern = " OR ".join(keywords)
    conn = _get_conn()
    rows = conn.execute(
        "SELECT id, title, url, ts FROM posts_fts WHERE posts_fts MATCH ? ORDER BY ts DESC LIMIT 50",
        (pattern,),
    ).fetchall()
    conn.close()
    return [dict(id=r[0], title=r[1], url=r[2], ts=r[3]) for r in rows]


def store_matches(post_id: str, keywords: List[str]):
    ts = dt.datetime.utcnow().isoformat()
    conn = _get_conn()
    for kw in keywords:
        conn.execute(
            "INSERT INTO matches(post_id, keyword, ts) VALUES(?,?,?)", (post_id, kw, ts)
        )
    conn.commit()
    conn.close()


def fetch_recent_matches(limit: int = 50):
    conn = _get_conn()
    rows = conn.execute(
        "SELECT m.ts, m.keyword, p.title, p.url FROM matches m JOIN posts p ON m.post_id = p.id ORDER BY m.ts DESC LIMIT ?",
        (limit,),
    ).fetchall()
    conn.close()
    return [dict(ts=r[0], keyword=r[1], title=r[2], url=r[3]) for r in rows]
