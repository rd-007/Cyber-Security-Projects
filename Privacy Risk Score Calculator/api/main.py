"""FastAPI app for privacy score."""
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List, Dict, Any
import tempfile, os
from scorlib import parse_permissions, calculate_score, load_weights

app = FastAPI(title="Privacy Risk Score Calculator")


@app.post("/score")
async def score(manifest: UploadFile = File(...)) -> Dict[str, Any]:
    if manifest.content_type not in {"text/xml", "application/xml", "text/plain"}:
        raise HTTPException(status_code=400, detail="Only XML or plain text permission list accepted")
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await manifest.read())
        tmp_path = tmp.name
    try:
        perms = parse_permissions(tmp_path)
    except Exception as e:
        os.remove(tmp_path)
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
    score, breakdown = calculate_score(perms)
    return {"score": score, "permissions": breakdown}
