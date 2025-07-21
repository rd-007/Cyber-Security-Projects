"""Compute hygiene score from raw check dict."""
from __future__ import annotations
from typing import Dict, Any, Tuple

WEIGHTS = {
    "days_since_patch": 0.5,  # -0.5 per day, capped at -40
    "firewall_enabled": 20,   # +20 if on
    "antivirus_present": 20,  # +20 if present
}


def compute_score(checks: Dict[str, Any]) -> Tuple[int, Dict[str, int]]:
    """Return overall 0–100 score and component contributions."""
    base = 40  # baseline
    contrib: Dict[str, int] = {}

    # Patch latency penalty
    days = checks.get("days_since_patch")
    if isinstance(days, int):
        penalty = min(days * WEIGHTS["days_since_patch"], 40)
        contrib["patch_penalty"] = -int(penalty)
    else:
        contrib["patch_penalty"] = -20  # unknown status

    # Firewall
    if checks.get("firewall_enabled"):
        contrib["firewall"] = WEIGHTS["firewall_enabled"]
    else:
        contrib["firewall"] = 0

    # Antivirus
    if checks.get("antivirus_present"):
        contrib["antivirus"] = WEIGHTS["antivirus_present"]
    else:
        contrib["antivirus"] = 0

    total = base + sum(contrib.values())
    total = max(0, min(100, total))
    return int(total), contrib
