"""Vectorisation utilities: TF-IDF on raw log lines."""
from sklearn.feature_extraction.text import TfidfVectorizer  # type: ignore
from typing import List

_vectorizer: TfidfVectorizer | None = None


def get_vectorizer() -> TfidfVectorizer:
    global _vectorizer
    if _vectorizer is None:
        _vectorizer = TfidfVectorizer(analyzer="word", token_pattern=r"\b\w+\b", max_features=5000)
    return _vectorizer


def vectorize_lines(lines: List[str]):
    vec = get_vectorizer()
    return vec.fit_transform(lines)
