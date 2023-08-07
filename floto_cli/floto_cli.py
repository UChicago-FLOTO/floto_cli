import click
from device_cmds import device_cli
from collection_cmd import collection_cli
from auth_cmd import auth_cli
from application_cmd import application_cli
from job_cmd import job_cli

cli = click.CommandCollection(sources=[device_cli, auth_cli, collection_cli, application_cli, job_cli])

if __name__ == '__main__':
    cli()
