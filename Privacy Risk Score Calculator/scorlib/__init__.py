"""scorlib – permission parsing & scoring."""
from .parser import parse_permissions
from .score import calculate_score, load_weights

__all__ = [
    "parse_permissions",
    "calculate_score",
    "load_weights",
]
