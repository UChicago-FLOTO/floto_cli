import click
from device_cmds import device_cli
from collection_cmd import collection_cli
from auth_cmd import auth_cli
cli = click.CommandCollection(sources=[device_cli, auth_cli, collection_cli])

if __name__ == '__main__':
    cli()
