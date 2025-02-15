import typer

from rich import print
from rich.prompt import Prompt
from rich.markup import escape

app = typer.Typer()


@app.command()
def install():
    print("[bold red]Not Implemented[/bold red]")
    raise typer.Abort()


@app.command()
def configure():
    pick_location()


def pick_location():
    try:
        location = Prompt.ask(
            "[yellow]Where[/yellow] would you like your server to be created at?\n[grey0](Default: /opt/minecraft)[/grey0]"
        )
    except KeyboardInterrupt:
        print("\n")
        raise typer.Abort()
    if location == "":
        location = "/opt/minecraft"
    print(f"Selected [bold magenta]{escape(location)}[/bold magenta]")


if __name__ == "__main__":
    app()
