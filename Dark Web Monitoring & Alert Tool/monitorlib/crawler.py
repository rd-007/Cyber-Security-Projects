"""Simple async crawler pulling RSS/HTML from paste site mirrors."""
from __future__ import annotations
import asyncio
import httpx
from bs4 import BeautifulSoup  # type: ignore
from typing import List, Tuple
from .storage import store_post
import hashlib

FEEDS = [
    # Public clear-web mirrors of leak/paste sites (examples)
    "https://ransomwatch.telemetry.ltd/feed/",  # ransomware leaks RSS
    "https://pastebin.com/archive",  # HTML example (not dark web but demo)
]

HEADERS = {"User-Agent": "DarkMonitor/0.1"}


async def _fetch_rss(client: httpx.AsyncClient, url: str):
    r = await client.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "xml")
    for item in soup.find_all("item"):
        title = item.title.text if item.title else "(no title)"
        link = item.link.text if item.link else url
        desc = item.description.text if item.description else ""
        pid = hashlib.sha1(link.encode()).hexdigest()
        store_post(pid, title, link, desc)


async def fetch_feeds_once():
    async with httpx.AsyncClient(headers=HEADERS) as client:
        tasks = [_fetch_rss(client, f) for f in FEEDS]
        await asyncio.gather(*tasks)
