"""Feature extraction for URLs.
This keeps it lightweight & explainable.
"""
from __future__ import annotations

import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup  # type: ignore
import tldextract


def extract_features(url: str):
    """Return a dict of handcrafted features for ML model."""
    parsed = urlparse(url)
    ext = tldextract.extract(url)
    hostname = parsed.netloc.lower()

    feats = {
        # structural length-based
        "url_length": len(url),
        "hostname_length": len(hostname),
        "path_length": len(parsed.path),
        "num_dots": url.count("."),
        "num_hyphens": url.count("-"),
        # lexical patterns
        "has_at_symbol": "@" in url,
        "has_ip": bool(re.match(r"^(?:http[s]?://)?(?:\d{1,3}\.){3}\d{1,3}", url)),
        "num_digits": sum(c.isdigit() for c in url),
        # domain-related
        "subdomain_length": len(ext.subdomain),
        "tld": ext.suffix,
    }
    return feats
