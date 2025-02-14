import typer
from rich import print
from rich.prompt import Prompt

app = typer.Typer()


@app.command()
def main():
    test = Prompt.ask("Test")
    print(f"[red][bold]{test}")


if __name__ == "__main__":
    app()
