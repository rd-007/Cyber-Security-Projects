"""phishlib: Core phishing detection utilities."""
from importlib.resources import files
from pathlib import Path
from typing import List, Tuple

from .features import extract_features
from .model import load_model

__all__ = [
    "classify_url",
    "batch_classify",
]

_model = None


def _get_model():
    global _model
    if _model is None:
        _model = load_model()
    return _model


def classify_url(url: str) -> Tuple[str, float]:
    """Classify a single URL.

    Returns (label, probability_of_phishing).
    """
    feats = extract_features(url)
    model = _get_model()
    prob_phish = float(model.predict_proba([feats])[0, 1])
    label = "phishing" if prob_phish >= 0.5 else "benign"
    return label, prob_phish


def batch_classify(urls: List[str]):
    model = _get_model()
    feats = [extract_features(u) for u in urls]
    probs = model.predict_proba(feats)[:, 1]
    return [
        {
            "url": u,
            "label": "phishing" if p >= 0.5 else "benign",
            "probability": float(p),
        }
        for u, p in zip(urls, probs)
    ]
