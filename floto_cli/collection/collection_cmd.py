import json

import click
import requests
import os

url = os.getenv("FLOTO_DOMAIN", "https://portal.floto.science/api")
temp_token = os.getenv("FLOTO_TOKEN", "")


@click.group('collection_cli')
@click.pass_context
def collection_cli(ctx):
    pass


@collection_cli.group('collection')
def collection():
    pass

@collection.command("collections")
def collections():
    click.echo("List collections: ")
    resp = requests.get(url=url + "/collections/")
    return resp

@collection.command("details")
@click.argument("uuid")
def details(uuid):
    click.echo("Collection details")
    resp = requests.get(url=url + "/collections/" + uuid)
    return resp

@collection.command("create")
@click.argument("name")
@click.option('--is_public', '-up', default=False, type=bool)
@click.option('--description', '-d', required=False, type=str)
def create(name, is_public, description):
    click.echo("Collection create")
    data = {
        "name": name,
        "is_public": is_public,
        "description": description
    }
    data = json.dumps(data)
    resp = requests.post(url=url+"/collections", json=data)
    return resp

@collection.command("update")
@click.argument("name")
@click.option('--is_public', '-up', default=False, type=bool)
@click.option('--description', '-d', required=False, type=str)
def update(name, is_public, description):
    click.echo("Collection update")
    data = {
        "name": name,
        "is_public": is_public,
        "description": description
    }
    data = json.dumps(data)
    resp = requests.post(url=url+"/collections", json=data)
    return resp

@collection.command("delete")
@click.argument("uuid")
def delete(uuid):
    click.echo("Collection delete")
    resp = requests.delete(url=url+"/collections/"+uuid)
    return resp