"""FastAPI endpoint for log anomaly detection."""
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List, Dict, Any
import tempfile
import os

from anomlib import predict_file

app = FastAPI(title="Log Anomaly Detector")


@app.post("/scan")
async def scan(file: UploadFile = File(...)) -> List[Dict[str, Any]]:
    if file.content_type not in {"text/plain", "application/octet-stream"}:
        raise HTTPException(status_code=400, detail="Only text files supported")
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    try:
        results = predict_file(tmp_path)
    finally:
        os.remove(tmp_path)
    return results
