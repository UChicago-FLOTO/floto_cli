import json
import os

import click
import requests

import config_handler
from device_model import Device
from device_model import make_devices_table
from rich.console import Console

# url = "https://portal.floto.science/api"
url = "http://localhost:8080/api"
temp_token = os.getenv("FLOTO_TOKEN", "")
sessionId = 'sessionid'
csrftoken = 'csrftoken'
cookie = {sessionId: config_handler.get_token()}
console = Console()


@click.group('device_cli')
@click.pass_context
def device_cli(ctx):
    pass


@device_cli.group('device')
def device():
    pass


@device.command('ls')
@click.option('--filter', '-f')
def ls(filter):
    # works
    resp = requests.get(url=url + "/devices", params={'filter': filter}, cookies=cookie)
    print(resp)
    device_data = resp.json()
    table = make_devices_table()
    device_list = [Device(**data) for data in device_data]
    for d in device_list:
        table.add_row(*d.make_row())
    console.print(table)
    return device_list


@device.command("details")
@click.argument("uuid")
@click.option('--filter', '-f')
def details(uuid, filter):
    # works
    resp = requests.get(url=url + "/devices/" + uuid, params={'filter': filter}, cookies=cookie)
    device = Device(**resp.json())
    console.log(device)
    return device


@device.command("logs")
@click.argument("uuid")
@click.option("--count", default=100)
@click.option('--filter', '-f')
def logs(uuid, count, filter):
    # /devices/uuid/logs/int
    # will work
    print(uuid, count)
    resp = requests.get(url=url + "/devices/" + uuid + "/logs/" + str(count), params={'filter': filter}, cookies=cookie)
    console.log(resp.json())
    return resp.json()


@device.command("command")
@click.argument("uuid")
@click.argument("cmd")
def command(uuid, cmd):
    # /devices/uuid/command
    # works
    data = {
        "command": cmd
    }
    resp = requests.post(url=url + "/devices/" + uuid + "/command/", json=json.dumps(data), cookies=cookie)
    print(resp.request.url)
    print(resp)


@device.command("updateEnv")
@click.argument("uuid")
@click.option("--env", multiple=True)
def updateEnv(uuid, env):
    print("Env:", env, " ", type(env))
    # no work
    data = json.dumps(env)
    resp = requests.put(url=url + "/devices/" + uuid + "/env", json=data, cookies=cookie)
    print(resp.request.url)
    print(resp)


@device.command("action")
@click.argument("uuid")
@click.option('--action', type=click.Choice(['BLINK', 'RESTART', 'SHUTDOWN']), required=True)
def action(uuid, action):
    # no work
    click.echo("Action:", action)
    click.echo("UUID: ", uuid)
    data = json.dumps(action)
    resp = requests.post(url=url + "/devices/" + uuid + "/action", json=data, cookies=cookie)
    click.echo(resp.json())


@device.command("addEnv")
@click.argument("uuid")
@click.argument("envs", nargs=-1)
def addEnv(uuid, envs):
    print("Env:", envs, " ", type(envs))
    data = dict([env.split("=") for env in envs])
    data['uuid'] = uuid
    # no work
    data = json.dumps(data)
    print(data)
    resp = requests.post(url=url + "/envs/", json=data, cookies=cookie)
    print(resp.status_code)
    # print(resp.text)
    return resp


@device.command("rmEnv")
@click.argument("uuid")
@click.argument("env")
def rmEnv(uuid, env):
    print("Rm Env: ", env, " ", type(env))
    data = json.dumps(env)
    resp = requests.delete(url=url + '/envs/' + uuid + '/', json=data, cookies=cookie)
    print(resp.status_code)
    print(resp.text)


@device.command("lsEnv")
@click.argument("uuid")
def lsEnv(uuid):
    print("ls Env: ", uuid)
    resp = requests.get(url=url + '/envs/'+uuid+"/", cookies=cookie)
    print(resp.status_code)
    print(resp.text)

