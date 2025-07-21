"""Model training/loading and file-level prediction utilities."""
from __future__ import annotations

import pickle
from pathlib import Path
from typing import List, Dict, Any

from sklearn.ensemble import IsolationForest  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer  # type: ignore

MODEL_PATH = Path(__file__).resolve().parent / "_model.pkl"


def train_or_load_model(lines: List[str]) -> Pipeline:
    """Train a new IsolationForest if no saved model, else load existing one."""
    if MODEL_PATH.exists():
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)

    vec = TfidfVectorizer(analyzer="word", token_pattern=r"\b\w+\b", max_features=5000)
    clf = IsolationForest(n_estimators=200, contamination="auto", random_state=42)
    pipe: Pipeline = Pipeline([("vec", vec), ("clf", clf)])
    pipe.fit(lines)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(pipe, f)
    return pipe


def predict_file(filepath: str, threshold: float = -0.2):
    """Return list of dicts with line number, content, and anomaly score (<threshold is anomaly)."""
    with open(filepath, "r", errors="ignore") as f:
        lines = [l.rstrip("\n") for l in f]

    model = train_or_load_model(lines[:10000])  # train on first 10k lines
    scores = model.decision_function(lines)

    results: List[Dict[str, Any]] = []
    for idx, (line, score) in enumerate(zip(lines, scores), 1):
        if score < threshold:
            results.append({"line": idx, "score": float(score), "content": line})
    return results
