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


@click.group('application_cli')
@click.pass_context
def application_cli(ctx):
    pass


@application_cli.group('application')
def application():
    pass


@application.command('create')
@click.argument('container_ref')
@click.argument('name')
@click.argument('description')
@click.argument('environment')
@click.argument('is_public')
def create_application(container_ref, name, description, environment, is_public):
    body = {
        'container_ref': container_ref,
        'name': name,
        'description': description,
        'environment': environment,
        'is_public': is_public
    }
    resp = requests.post(url=url + '/applications', data=body, cookies=cookie)
    print(resp.status_code)
    print(resp.text)


@application.command('ls')
def list_applications():
    resp = requests.get(url=url+'/applications', cookies=cookie)
    print(resp.status_code)
    print(resp.text)

@application.command('details')
@click.argument('app_uuid')
def details_application(app_uuid):
    resp = requests.put(url=url+'/applications/'+app_uuid, cookies=cookie)
    print(resp.status_code)
    print(resp.text)

@application.command('update')
@click.argument('app_uuid')
@click.argument('container_ref')
@click.argument('name')
@click.argument('description')
@click.argument('environment')
@click.argument('is_public')
def update_application(app_uuid, container_ref, name, description, environment, is_public):
    body = {
        'container_ref': container_ref,
        'name': name,
        'description': description,
        'environment': environment,
        'is_public': is_public
    }
    resp = requests.put(url=url+'/applications/'+app_uuid, data=body, cookies=cookie)
    print(resp.status_code)
    print(resp.text)

@application.command('delete')
@click.argument('app_uuid')
def delete_app(app_uuid):
    resp = requests.delete(url=url+'/applications/'+app_uuid, cookies=cookie)
    print(resp.status_code)
    print(resp.text)