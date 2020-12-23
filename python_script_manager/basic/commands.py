import click
from prettytable import PrettyTable
from .funcs import *
from .. import const

@click.group()
def basic():
    pass

# Initialize psm
@basic.command(name="init")
@click.option('-t', '--template', 'template', default='blank',help="Name of template")
def init_command(**kwargs):
    """Initialize PSM in current folder"""
    template = kwargs.pop('template')
    initialize(template)


# Run script
@basic.command(name="run")
@click.argument('name', required=True)
def run_command(**kwargs):
    """Run PSM script with NAME"""
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to run')
    runScript(name)

# Add script
@basic.command(name="add")
@click.option('-n', '--name', 'name', required=False,help="Name for new script")
@click.option('-c', '--command', 'command', required=False,help="Command that script will used for")
@click.option('-d', '--description', 'description', required=False,help="Description for new script (optional)")
def add_command(**kwargs):
    """Add new script"""
    name = kwargs.pop('name')
    command = kwargs.pop('command')
    description = kwargs.pop('description')
    while not name:
        name = input('Enter name for script: ')
    while not command:
        command = input('Enter command for script: ')
    if not description:
        description = input('Enter description for script (optional):')
    addScript(name, command, description)


@basic.command(name="list")
def list_command(**kwargs):
    """Generate list of scripts as table"""
    cmds = PrettyTable()
    cmds.field_names = ['Name', 'Command', 'Description']
    scripts = loadScripts()
    for name, data in scripts.items():
        row = (name, data["command"], data["description"])
        cmds.add_row(row)
    cmds.align = 'l'
    click.echo(cmds)


@basic.command(name="rm")
@click.option('-n', '--name', 'name', required=False,help="Name of script to remove")
def rm_command(**kwargs):
    """Remove script"""
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to remove: ')
    removeScript(name)


@basic.command(name="build")
def build_command(**kwargs):
    """Special script that will execute "psm run build" """
    runScript('build')


@basic.command(name="start")
def start_command(**kwargs):
    """Special script that will execute "psm run start" """
    runScript('start')


@basic.command(name="deploy")
def deploy_command(**kwargs):
    """Special script that will execute "psm run deploy" """
    runScript('deploy')
