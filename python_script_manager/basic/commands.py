import click
from prettytable import PrettyTable
from .funcs import *
from .. import const

@click.group()
def basic():
    pass

# Initialize psm
@basic.command()
@click.option('-t', '--template', 'template', default='blank',help="Name of template")
def init(**kwargs):
    """Initialize PSM in current folder"""
    template = kwargs.pop('template')
    initialize(template)


# Run script
@basic.command()
@click.argument('name', required=True)
def run(**kwargs):
    """Run PSM script with NAME"""
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to run')
    runScript(name)

# Add script
@basic.command()
@click.option('-n', '--name', 'name', required=False,help="Name for new script")
@click.option('-c', '--command', 'command', required=False,help="Command that script will used for")
@click.option('-d', '--description', 'description', required=False,help="Description for new script (optional)")
def add(**kwargs):
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


@basic.command()
def list(**kwargs):
    """Generate list of scripts as table"""
    cmds = PrettyTable()
    cmds.field_names = ['Name', 'Command', 'Description']
    scripts = loadScripts()
    for name, data in scripts.items():
        row = (name, data["command"], data["description"])
        cmds.add_row(row)
    cmds.align = 'l'
    click.echo(cmds)


@basic.command()
@click.option('-n', '--name', 'name', required=False,help="Name of script to remove")
def rm(**kwargs):
    """Remove script"""
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to remove: ')
    removeScript(name)


@basic.command()
def build(**kwargs):
    """Special script that will execute "psm run build" """
    runScript('build')


@basic.command()
def start(**kwargs):
    """Special script that will execute "psm run start" """
    runScript('start')


@basic.command()
def deploy(**kwargs):
    """Special script that will execute "psm run deploy" """
    runScript('deploy')
