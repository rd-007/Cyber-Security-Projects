"""FastAPI app exposing /scan endpoint."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import List

from phishlib import classify_url, batch_classify

app = FastAPI(title="Real-Time Phishing URL Detector")


class ScanRequest(BaseModel):
    url: HttpUrl | None = None
    urls: List[HttpUrl] | None = None

    def list_urls(self):
        if self.url:
            return [str(self.url)]
        if self.urls:
            return [str(u) for u in self.urls]
        raise ValueError("No URL(s) provided")


class ScanResult(BaseModel):
    url: str
    label: str
    probability: float


@app.post("/scan", response_model=List[ScanResult])
async def scan(req: ScanRequest):
    try:
        urls = req.list_urls()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    results = batch_classify(urls)
    return results
