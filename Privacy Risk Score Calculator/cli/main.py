"""CLI for privacy risk scoring."""
import typer
from rich import print
from rich.table import Table
from scorlib import parse_permissions, calculate_score, load_weights

app = typer.Typer(add_completion=False, help="Privacy Risk Score CLI")


@app.command()
def score(path: str):
    """Score a manifest file or plain-text permission list."""
    perms = parse_permissions(path)
    total, breakdown = calculate_score(perms)
    table = Table(title="Privacy Risk Breakdown")
    table.add_column("Permission")
    table.add_column("Weight", justify="right")
    for perm, w in breakdown:
        table.add_row(perm, str(w))
    print(table)
    print(f"[bold]Privacy Risk Score: {total}/100[/bold]")


if __name__ == "__main__":
    app()
