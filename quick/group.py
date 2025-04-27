import click


@click.group()
def cli():
    """命令组示例"""
    pass


@cli.command()
@click.option("--name", default="World", help="要问候的名称")
def hello(name):
    """问候某人"""
    click.echo(f"Hello {name}!")


@cli.command()
@click.argument("src")
@click.argument("dst")
def copy(src, dst):
    """复制文件"""
    click.echo(f"正在将 {src} 复制到 {dst}")


if __name__ == "__main__":
    cli()
