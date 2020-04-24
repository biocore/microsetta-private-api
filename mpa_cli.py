import click
from microsetta_private_api.server import build_app, run


@click.command()
def cli():
    app = build_app()
    run(app)
