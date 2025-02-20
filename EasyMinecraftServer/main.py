import typer
import json
import os
import psutil

from pathvalidate import sanitize_filepath
from rich import print
from rich.prompt import Prompt, Confirm
from rich.markup import escape
from util.version_list import versions
from pathlib import Path

app = typer.Typer()


@app.command()
def install():
    print("[bold red]Not Implemented[/bold red]")
    raise typer.Abort()


@app.command()
def configure():
    conf_dir: str = setup()
    location: str = pick_location()
    version: str = pick_version()
    loader: str = pick_server()
    ram: int = detect_ram()
    optimized: bool = is_optimized()
    open_port: bool = should_open_port()

    config = {
        "location": location,
        "version": version,
        "loader": loader,
        "ram": ram,
        "optimized": optimized,
        "open_port": open_port,
    }
    with open(f"{conf_dir}/config.json", mode="w", encoding="utf-8") as conf_file:
        json.dump(config, conf_file)
    # conf_dir: str, location: str, version: str, loader: str, ram: int, optimized: bool, open_port: bool


def setup():  # Create a default directory for the config file
    system = os.name
    if system == "posix":
        directory = "/opt/easymcserver/config"
        dir = Path(directory)
        dir.mkdir(parents=True, exist_ok=True)
        return directory
    elif system == "nt":
        homepath = os.getenv("HOMEPATH")
        directory = f"{homepath}/easymcserver/config"
        dir = Path(directory)
        dir.mkdir(parents=True, exist_ok=True)
        return directory


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
    location = sanitize_filepath(
        file_path=location, platform="auto"
    )  # Sanitize File Path
    print(f"Selected [bold magenta]{escape(location)}[/bold magenta]")
    return location  # Return location as string


def pick_version():
    try:
        version = Prompt.ask(
            "[yellow]Which version[/yellow] would you like your server to be?\n[grey0](Default: latest)[/grey0]"
        )
    except KeyboardInterrupt:
        print("\n")
        raise typer.Abort()
    if (
        version not in versions and version != ""
    ):  # Exit if version isn't in the versions list or empty
        print(f'[bold red]Version "{escape(version)}" is not supported![/bold red]')
        raise typer.Abort()
    if version == "":  # Set Default for Empty Strings
        version = "latest"
    print(f"Selected [bold magenta]{escape(version)}[/bold magenta]")
    return version  # Return version as string


def pick_server():
    # Return value for debug purposes only
    return "vanilla"  # Return software as string


def detect_ram():
    memory_info = psutil.virtual_memory().total
    total_ram = memory_info / (1024 * 1024)  # Bytes to Megabytes
    usable_ram = total_ram - 1024  # Removing 1 GB Ram for use by OS
    return usable_ram  # Return Megabytes as integer


def is_optimized():
    try:
        optimized = Confirm.ask(
            "Would you like your server to be [yellow]optimized[/yellow]?", default=True
        )
    except KeyboardInterrupt:
        print("\n")
        raise typer.Abort()
    return optimized  # Return true or false as boolean


def should_open_port():
    try:
        open_port = Confirm.ask(
            "Would you like the script to detect the firewall and open ports for you?",
            default=False,
        )
    except KeyboardInterrupt:
        print("\n")
        raise typer.Abort()
    return open_port  # Return true or false as boolean


if __name__ == "__main__":
    app()
