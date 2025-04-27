import click


@click.command()
@click.option("--verbose", "-v", is_flag=True, help="启用详细输出")
@click.option("--name", "-n", default="World", help="要问候的名称")
@click.option("--count", "-c", type=int, default=1, help="问候次数")
def hello(verbose, name, count):
    """示例命令演示选项用法"""
    if verbose:
        click.echo(f"将问候{name} {count}次")
    for _ in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello()
