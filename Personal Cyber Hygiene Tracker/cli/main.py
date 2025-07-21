"""CLI for personal cyber hygiene tracker."""
import typer
from rich import print
from rich.table import Table
from trackerlib import run_checks, compute_score, save_result, fetch_history

app = typer.Typer(add_completion=False, help="Cyber Hygiene Tracker CLI")


@app.command()
def check():
    """Run checks and display current hygiene score."""
    checks = run_checks()
    score, contrib = compute_score(checks)
    save_result(score, contrib)

    table = Table(title="Current Hygiene Report")
    table.add_column("Metric")
    table.add_column("Value")
    for k, v in checks.items():
        table.add_row(k, str(v))
    table.add_row("Score", str(score))
    print(table)


@app.command()
def history(limit: int = 10):
    """Show recent score history."""
    rows = fetch_history(limit)
    table = Table(title=f"Last {limit} Scores")
    table.add_column("Timestamp (UTC)")
    table.add_column("Score")
    for ts, s in rows:
        table.add_row(ts, str(s))
    print(table)


if __name__ == "__main__":
    app()
