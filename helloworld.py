import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", default="world", prompt="Your name", help="The person to greet.")
def main(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")


if __name__ == '__main__':
    import sys

    print(sys.argv)
    main()
