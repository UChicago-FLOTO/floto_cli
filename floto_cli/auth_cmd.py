import click
import os
import config_handler

@click.group('auth_cli')
@click.pass_context
def auth_cli(ctx):
    pass


@auth_cli.group('auth')
def auth():
    pass


@auth.command()
@click.option("--username", '-u', default=lambda: os.environ.get("FLOTO_USERNAME", ""))
@click.option("--password", '-p', hide_input=True, confirmation_prompt=True,
              default=lambda: os.environ.get("FLOTO_PASSWORD", ""))
@click.option('--token', '-t', default=lambda: os.environ.get("FLOTO_TOKEN", "token"), required=True)
def login(username, password, token):
    click.echo("Auth login completed")
    return config_handler.save_token(token)