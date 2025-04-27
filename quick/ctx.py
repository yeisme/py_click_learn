import click


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def cli(ctx, debug):
    """设置共享上下文"""
    ctx.ensure_object(dict)
    ctx.obj["DEBUG"] = debug


@cli.command()
@click.pass_context
def sync(ctx):
    """同步命令"""
    click.echo(f"同步模式，调试状态: {ctx.obj['DEBUG']}")


@cli.command()
@click.pass_context
def process(ctx):
    """处理命令"""
    click.echo(f"处理模式，调试状态: {ctx.obj['DEBUG']}")


if __name__ == "__main__":
    cli(obj={})
