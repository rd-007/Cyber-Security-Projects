"""trackerlib – system checks and scoring."""
from .checks import run_checks
from .storage import save_result, fetch_history
from .score import compute_score

__all__ = [
    "run_checks",
    "compute_score",
    "save_result",
    "fetch_history",
]
