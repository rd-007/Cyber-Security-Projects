"""Lightweight system checks for Windows cyber hygiene.
Note: Some checks need admin privileges or may fail on non-Windows OS – handle gracefully.
"""
from __future__ import annotations
import datetime as dt
import platform
from typing import Dict, Any
import psutil  # type: ignore

try:
    import wmi  # type: ignore
except ImportError:  # pragma: no cover
    wmi = None  # type: ignore


def _windows_updates_last_date() -> dt.datetime | None:
    if not wmi:
        return None
    c = wmi.WMI()
    hotfixes = c.Win32_QuickFixEngineering()
    dates = []
    for h in hotfixes:
        try:
            dates.append(dt.datetime.strptime(h.InstalledOn, "%m/%d/%Y"))
        except Exception:
            continue
    return max(dates) if dates else None


def _firewall_enabled() -> bool | None:
    if platform.system() != "Windows":
        return None
    # Check if MpsSvc (Windows Firewall) service is running
    for svc in psutil.win_service_iter():
        if svc.name().lower() == "mpssvc":
            return svc.status() == "running"
    return None


def _antivirus_running() -> bool | None:
    if not wmi:
        return None
    c = wmi.WMI(namespace="root\\SecurityCenter2")
    avs = c.AntiVirusProduct()
    return bool(avs)


def run_checks() -> Dict[str, Any]:
    """Return dict with raw check results."""
    checks: Dict[str, Any] = {}
    checks["os"] = platform.platform()

    last_patch = _windows_updates_last_date()
    if last_patch:
        checks["days_since_patch"] = (dt.datetime.now() - last_patch).days
    else:
        checks["days_since_patch"] = None

    checks["firewall_enabled"] = _firewall_enabled()
    checks["antivirus_present"] = _antivirus_running()

    # Add more checks later (disk encryption, open ports, etc.)
    return checks
