"""CLI for log anomaly detection."""
import typer
from rich import print
from rich.table import Table
from anomlib import predict_file

app = typer.Typer(add_completion=False, help="Log Anomaly Detector CLI")


@app.command()
def scan(path: str, threshold: float = -0.2):
    """Scan a log file and print anomalous lines."""
    results = predict_file(path, threshold=threshold)
    table = Table(title=f"Anomalies in {path}")
    table.add_column("Line #", style="cyan")
    table.add_column("Score", style="magenta")
    table.add_column("Content", style="white")
    for r in results:
        table.add_row(str(r["line"]), f"{r['score']:.3f}", r["content"][:120])
    print(table)
    print(f"[bold]{len(results)} anomalies found[/bold]")


if __name__ == "__main__":
    app()
