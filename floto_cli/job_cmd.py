import click
import requests
from rich.console import Console
import os
import config_handler

url = "http://localhost:8080/api"
temp_token = os.getenv("FLOTO_TOKEN", "")
sessionId = 'sessionid'
csrftoken = 'csrftoken'
cookie = {sessionId: config_handler.get_token()}
console = Console()


@click.group('job_cli')
@click.pass_context
def job_cli(ctx):
    pass


@job_cli.group('job')
def job():
    pass


@job.command('create')
@click.argument('start_timestamp')
@click.argument('end_timestamp')
@click.argument('application_id')
@click.argument('environment')
@click.argument('devices', nargs=1)
def create_job(start_timestamp, end_timestamp, application_id, environment, devices):
    body = {
        'application_id': application_id,
        'environment': environment,
        'timing': [start_timestamp, end_timestamp],
        'devices': devices
    }

    resp = requests.post(url=url + '/jobs', data=body, cookies=cookie)
    print(resp.status_code)
    print(resp.text)


@job.command('ls')
def list_jobs():
    resp = requests.get(url=url + '/jobs', cookies=cookie)
    print(resp.status_code)
    print(resp.text)


@job.command('details')
@click.argument('job_uuid')
def details_job(job_uuid):
    resp = requests.get(url=url + '/jobs/' + job_uuid, cookies=cookie)
    print(resp.status_code)
    print(resp.text)


@job.command('delete')
@click.argument('job_uuid')
def delete_job(job_uuid):
    resp = requests.delete(url=url + '/jobs/' + job_uuid, cookies=cookie)
    print(resp.status_code)
    print(resp.text)
