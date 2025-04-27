import click


@click.command()
@click.argument("name")
@click.argument("count", type=int, default=1)
def hello(name, count):
    """示例命令演示参数用法"""
    for _ in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello()
