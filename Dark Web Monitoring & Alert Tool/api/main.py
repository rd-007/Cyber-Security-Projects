"""FastAPI endpoints for Dark Web Monitoring."""
from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
from monitorlib import init_db, search_keywords, fetch_recent_matches

app = FastAPI(title="Dark Web Monitoring & Alert Tool")

init_db()


@app.get("/search")
async def search(q: str) -> List[Dict[str, Any]]:
    if not q:
        raise HTTPException(status_code=400, detail="Keyword required")
    keywords = [k.strip() for k in q.split(",") if k.strip()]
    return search_keywords(keywords)


@app.get("/alerts")
async def alerts(limit: int = 20):
    return fetch_recent_matches(limit)
