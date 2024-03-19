"""Console script for mydocs.domain.example."""

import sys
import typer

app = typer.Typer()

@app.command()
def main(args=None):
    """Console script for mydocs.domain.example."""
    typer.echo("Replace this message by putting your code into mydocs.domain.example.cli.main")
    typer.echo("See typer documentation at https://typer.tiangolo.com/")
    return 0




if __name__ == "__main__":
    sys.exit(app())
