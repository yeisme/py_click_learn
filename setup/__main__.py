import click
import os


@click.group()
def cli():
    pass


@cli.command()
def ls():
    os.system("ls")


@cli.command()
def pwd():
    os.system("pwd")


@cli.command()
def echo():
    os.system("echo")


@cli.command()
def file():
    os.system("ls -a")


@cli.command()
def dir():
    os.system("ls -l")


if __name__ == "__main__":
    cli()
