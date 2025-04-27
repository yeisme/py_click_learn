import click


@click.command()
@click.option("--int-value", type=int)
@click.option("--float-value", type=float)
@click.option("--bool-value", is_flag=True)
@click.option("--choice", type=click.Choice(["one", "two", "three"]))
@click.option("--file", type=click.File("r"))
@click.option("--path", type=click.Path(exists=True))
def process(
    int_value: int,
    float_value: float,
    bool_value: bool,
    choice: str,
    file: click.File,
    path: click.Path,
):
    """展示不同的参数类型"""
    click.echo(f"整数: {int_value}")
    click.echo(f"浮点数: {float_value}")
    click.echo(f"布尔值: {bool_value}")
    click.echo(f"选项: {choice}")
    click.echo(f"文件内容: {file.read() if file else 'No file'}")
    click.echo(f"路径: {path}")


if __name__ == "__main__":
    process()
