import typer
from .containers import list

app = typer.Typer()
app.command()(list)

if __name__ == "__main__":
    app()