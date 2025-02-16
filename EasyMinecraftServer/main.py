import typer
import json

from pathvalidate import sanitize_filepath
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
    location = pick_location()

    # config = {"location": location, "version": version, "loader": loader, "ram": ram, "optimized": optimized}
    # with open("config.json", mode="w", encoding="utf-8") as conf_file:
    #   json.dump(config, conf_file)
    json.dump()
    # location: str, version: str, loader: str, ram: int, optimized: bool


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
    location = sanitize_filepath(file_path=location, platform="auto")
    print(f"Selected [bold magenta]{escape(location)}[/bold magenta]")
    return location


if __name__ == "__main__":
    app()
