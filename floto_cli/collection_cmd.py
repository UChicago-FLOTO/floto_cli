import json

import click
import requests
import os
import config_handler

url = "https://portal.floto.science/api"
cookie = config_handler.get_token()
sessionId = 'sessionid'
csrftoken = 'csrftoken'
cookie = {sessionId: config_handler.get_token()}


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
    resp = requests.get(url=url + "/collections/", cookies=cookie)
    print(resp)
    print(resp.json())
    return resp


@collection.command("details")
@click.argument("uuid")
def details(uuid):
    click.echo("Collection details")
    resp = requests.get(url=url + "/collections/" + uuid, cookies=cookie)
    print(resp)
    print(resp.json())
    return resp

@collection.command("list")
def list():
    click.echo("Collection list")
    resp = requests.get(url=url+"/collections", cookies=cookie)
    print(resp)
    print(resp.json())


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
    resp = requests.post(url=url + "/collections", json=data, cookies=cookie)
    print(resp)
    print(resp.json())
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
    resp = requests.put(url=url + "/collections", json=data, cookies=cookie)
    return resp


@collection.command("delete")
@click.argument("uuid")
def delete(uuid):
    click.echo("Collection delete")
    resp = requests.delete(url=url + "/collections/" + uuid, cookies=cookie)
    return resp
