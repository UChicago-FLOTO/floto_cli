import click
import os
from device.device_cmds import device_cli
from authentication import auth_cmd
from collection.collection_cmd import collection_cli
from authentication.auth_cmd import auth_cli
cli = click.CommandCollection(sources=[device_cli, auth_cli, collection_cli])

if __name__ == '__main__':
    cli()
