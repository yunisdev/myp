import click
from typing import Tuple
from prettytable import PrettyTable
from .funcs import (
    addScript,
    removeScript
)
from .. import const
from ..globals import (
    process_unknown_options,
    runScript,
    runScriptIfExist,
    loadScripts
)
from ..__main__ import main


# Run script
@main.command("run", context_settings=const.CONTEXT_SETTINGS)
@click.argument('name', required=True)
@click.pass_context
def run_command(ctx: click.Context, name: str):
    """Run PSM script with NAME"""
    runScript(name, unknown_options=process_unknown_options(ctx.__dict__["args"]))


# Add script
@main.command("add")
@click.option('-n', '--name', 'name', help="Name for new script", prompt="Enter name for script")
@click.option('-c', '--command', 'command', help="Command that script will used for", prompt="Enter command for script")
@click.option('-d', '--description', 'description', help="Description for new script (optional)", prompt="Enter description for script", default="")
def add_command(name: str, command: str, description: str):
    """Add new script"""
    addScript(name, command, description)


# List scripts
@main.command("list")
def list_command():
    """Generate list of scripts as table"""
    cmds: PrettyTable = PrettyTable()
    cmds.field_names = ['Name', 'Command', 'Description']
    scripts: dict = loadScripts()
    for name, data in scripts.items():
        row: Tuple[str, str, str] = (name, data["command"], data["description"])
        cmds.add_row(row)
    cmds.align = 'l'
    click.echo(cmds)


# Remove script
@main.command("rm")
@click.option('-n', '--name', 'name', required=True, help="Name of script to remove", prompt='Enter name of script to remove')
def rm_command(name: str):
    """Remove script"""
    removeScript(name)


# Special Scripts
@main.command("build")
def build_command():
    """Special script that will execute "psm run build" """
    runScript('build')


@main.command("test")
def test_command():
    """Special script that will execute "psm run test" """
    runScript('test')


@main.command("start")
def start_command():
    """Special script that will execute "psm run start" """
    runScript('start')


@main.command("deploy")
@click.option('-b', '--build', 'build', is_flag=True, help="Build before deploy")
def deploy_command(build: bool):
    """Special script that will execute "psm run deploy" """
    if build:
        runScript('build')
    runScriptIfExist('predeploy')
    runScript('deploy')
    runScriptIfExist('postdeploy')
