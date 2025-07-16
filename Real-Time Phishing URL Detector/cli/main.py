"""Typer-based CLI wrapper."""
import typer
from phishlib import classify_url

app = typer.Typer(add_completion=False, help="Real-Time Phishing URL Detector CLI")


@app.command()
def scan(url: str):
    """Scan a single URL and print label + probability."""
    label, prob = classify_url(url)
    typer.echo(f"{label.upper()} ({prob:.2%}) – {url}")


if __name__ == "__main__":
    app()
