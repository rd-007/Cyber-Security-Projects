"""Privacy risk scoring functions."""
from __future__ import annotations
import yaml
from pathlib import Path
from typing import Dict, List, Tuple

WEIGHTS_PATH = Path(__file__).resolve().parent.parent / "data" / "weights_default.yaml"


def load_weights(path: str | Path | None = None) -> Dict[str, int]:
    p = Path(path) if path else WEIGHTS_PATH
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)  # type: ignore[return-value]


def calculate_score(perms: List[str], weights: Dict[str, int] | None = None):
    """Return tuple (score0to100, breakdown list)."""
    weights = weights or load_weights()
    total_possible = sum(weights.values())
    present_score = 0
    breakdown: List[Tuple[str, int]] = []
    for p in perms:
        w = weights.get(p.upper(), 0)
        if w:
            present_score += w
            breakdown.append((p.upper(), w))
    score = int(round((present_score / total_possible) * 100)) if total_possible else 0
    return score, breakdown
