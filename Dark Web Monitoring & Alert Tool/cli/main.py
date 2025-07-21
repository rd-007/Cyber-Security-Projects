"""CLI for Dark Web Monitoring."""
import asyncio
import typer
from rich import print
from rich.table import Table
from monitorlib import fetch_feeds_once, search_keywords, init_db
from apscheduler.schedulers.asyncio import AsyncIOScheduler

app = typer.Typer(add_completion=False, help="Dark Web Monitoring CLI")


@app.command()
def watch(keywords: str, interval: int = 30):
    """Continuously crawl feeds every INTERVAL minutes and show matches for CSV KEYWORDS."""
    kws = [k.strip() for k in keywords.split(",") if k.strip()]

    async def job():
        await fetch_feeds_once()
        matches = search_keywords(kws)
        if matches:
            table = Table(title="Matches Found")
            table.add_column("Time")
            table.add_column("Keyword")
            table.add_column("Title")
            table.add_column("URL")
            for m in matches:
                table.add_row(m["ts"], ",".join(kws), m["title"][:40], m["url"])
            print(table)

    async def runner():
        init_db()
        sched = AsyncIOScheduler()
        sched.add_job(job, "interval", minutes=interval, next_run_time=None)
        sched.start()
        print(f"Watching feeds every {interval} min for: {', '.join(kws)}")
        while True:
            await asyncio.sleep(3600)

    asyncio.run(runner())


@app.command()
def search(keywords: str):
    """Manual search of stored posts."""
    kws = [k.strip() for k in keywords.split(",") if k.strip()]
    matches = search_keywords(kws)
    table = Table(title="Search Results")
    table.add_column("Time")
    table.add_column("Title")
    table.add_column("URL")
    for m in matches:
        table.add_row(m["ts"], m["title"][:50], m["url"])
    print(table)


if __name__ == "__main__":
    app()
