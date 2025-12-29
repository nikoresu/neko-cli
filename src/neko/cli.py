import typer

from greetings.cli import app as greetings_app
from containers.cli import app as containers_app

app = typer.Typer(help="Neko CLI — manage services and utilities")

# Mount sub-commands
app.add_typer(containers_app, name="containers")

if __name__ == "__main__":
    app()
