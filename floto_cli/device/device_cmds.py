import json
import os

import click
import requests
from .device_model import Device

url = os.getenv("FLOTO_DOMAIN", "https://portal.floto.science/api")
temp_token = os.getenv("FLOTO_TOKEN", "")


@click.group('device_cli')
@click.pass_context
def device_cli(ctx):
    pass


@device_cli.group('device')
def device():
    pass


@device.command('devices')
@click.option('--filter', '-f')
def devices(filter):
    # works
    resp = requests.get(url=url + "/devices", params={'filter': filter})
    click.echo("devices")
    return resp


@device.command("details")
@click.argument("uuid")
def details(uuid):
    # works
    click.echo("details uuid=" + uuid)
    resp = requests.get(url=url + "/devices/" + uuid, params={'filter': filter})
    return resp


@device.command("logs")
@click.argument("uuid")
@click.option("--count")
def logs(uuid, count):
    # /devices/uuid/logs/int
    # will work
    resp = requests.get(url=url + "/devices/" + uuid + "/logs/" + str(count), params={'filter': filter})
    click.echo("logs:uuid= " + uuid + " count=" + count)
    return resp


@device.command("command")
@click.argument("uuid")
@click.argument("cmd")
def command(uuid, cmd):
    # /devices/uuid/command
    # works
    data = {
        "command": cmd
    }
    resp = requests.post(url=url + "/devices/" + uuid + "/command", json=json.dumps(data))
    click.echo("Command:" + cmd)


@device.command("updateEnv")
@click.argument("uuid")
@click.option("--env", multiple=True)
def updateEnv(uuid, env):
    print("Env:", env, " ", type(env))
    # no work
    data = json.dumps(env)
    resp = requests.put(url=url + "/devices/" + uuid + "/env", json=data)
    click.echo("updateEnv:" + uuid)


@device.command("action")
@click.argument("uuid")
@click.option('--action', type=click.Choice(['BLINK', 'RESTART', 'SHUTDOWN']), required=True)
def action(uuid, action):
    # no work
    click.echo("Action:", action)
    click.echo("UUID: ", uuid)
    data = json.dumps(action)
    resp = requests.post(url=url + "/devices/" + uuid + "/action", json=data)
