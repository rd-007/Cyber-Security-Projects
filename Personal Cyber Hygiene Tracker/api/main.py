"""FastAPI service for hygiene tracker."""
from fastapi import FastAPI
from trackerlib import run_checks, compute_score, save_result, fetch_history
from typing import Dict, Any, List, Tuple

app = FastAPI(title="Personal Cyber Hygiene Tracker")


@app.get("/status")
async def status() -> Dict[str, Any]:
    checks = run_checks()
    score, contrib = compute_score(checks)
    save_result(score, contrib)
    return {"score": score, "checks": checks, "contributions": contrib}


@app.get("/history")
async def history(limit: int = 30) -> List[Tuple[str, int]]:
    return fetch_history(limit)
