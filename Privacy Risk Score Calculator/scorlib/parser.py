"""Permission extraction from AndroidManifest.xml or plain list."""
from __future__ import annotations
from typing import List
from pathlib import Path
from lxml import etree  # type: ignore

ANDROID_NS = "http://schemas.android.com/apk/res/android"


def _extract_from_android_manifest(path: Path) -> List[str]:
    tree = etree.parse(str(path))
    permissions = []
    for perm in tree.xpath("//uses-permission"):
        name = perm.get(f"{{{ANDROID_NS}}}name")
        if name and name.startswith("android.permission."):
            permissions.append(name.split(".")[-1])
    return permissions


def parse_permissions(source: str | List[str]):
    """Return list of permission strings (e.g., CAMERA, READ_SMS)."""
    if isinstance(source, list):
        return source
    path = Path(source)
    if not path.exists():
        raise FileNotFoundError(source)
    if path.name.endswith("AndroidManifest.xml"):
        return _extract_from_android_manifest(path)
    raise ValueError("Unsupported manifest type – supply AndroidManifest.xml or list")
