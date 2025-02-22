# Easy Minecraft Server

Easy Minecraft Server is a CLI app I'm developing to make creating Minecraft servers easy  
I hope to support all Minecraft versions and most mod loader/plugin frameworks

**Hybrid server JARs will not be added**
**Support for versions below 1.12.2 (except 1.7.10 for Forge) will not be provided. YOU ARE ON YOUR OWN**

# Development

## Requirements

- [Rust](https://www.rust-lang.org/) (Pre-Commit Hooks)
- [Golang](https://go.dev/) (Pre-Commit Hooks)
- [Prettier](https://prettier.io/) (IDE Extension)
- [Poetry](https://python-poetry.org/)

## Setup

After you install all the requirements, run these commands:

```
poetry shell
poetry install
pre-commit install
```

## Used sources

[NodeJS Minecraft Versions](https://github.com/Nixinova/Minecraft-Versions) by Nixinova ([java.yaml](https://github.com/Nixinova/Minecraft-Versions/blob/main/data/java.yaml))  
[Tips and Tricks on Optimization](https://www.setup.md/docs) by the r/admincraft Community ( [Reddit](https://www.reddit.com/r/admincraft/) | [Discord](https://discord.gg/DxrXq2R) )

## Used libraries

- [Typer](https://pypi.org/project/typer/)
- [pathvalidate](https://pypi.org/project/pathvalidate/)
- [psutil](https://pypi.org/project/psutil/)
