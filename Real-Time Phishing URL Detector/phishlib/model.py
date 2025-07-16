"""Model I/O utilities.
For the starter scaffold we ship a naive dummy model trained on handcrafted rules.
Later you can run `python -m data.train` to retrain a LogisticRegression model.
"""
from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any

from sklearn.dummy import DummyClassifier  # type: ignore
from sklearn.feature_extraction import DictVectorizer  # type: ignore
from sklearn.pipeline import Pipeline  # type: ignore

MODEL_PATH = Path(__file__).resolve().parent / "_model.pkl"


def _create_dummy_model():
    # Pipeline: vectorizer + dummy majority classifier
    vec = DictVectorizer(sparse=False)
    clf = DummyClassifier(strategy="most_frequent")
    return Pipeline([("vec", vec), ("clf", clf)])


def load_model() -> Any:
    """Return pipeline model, training a dummy one if none exists."""
    if MODEL_PATH.exists():
        with open(MODEL_PATH, "rb") as f:
            return pickle.load(f)
    model = _create_dummy_model()
    # Save for next time
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)
    return model
