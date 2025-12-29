import typer
from .containers import containers

app = typer.Typer()
app.command()(containers)

if __name__ == "__main__":
    app()