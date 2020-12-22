import sys
import click
import os
try:
    from .funcs import *
    from . import const
except ImportError:
    from funcs import *
    import const
from prettytable import PrettyTable


@click.group()
@click.version_option(const.version)
def main():
    pass


@main.command()
@click.option('-t', '--template', 'template', default='blank')
def init(**kwargs):
    template = kwargs.pop('template')
    initialize(template)


@main.command()
@click.argument('name', required=True)
def run(**kwargs):
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to run')
    runScript(name)


@main.command()
@click.option('-n', '--name', 'name', required=False)
@click.option('-c', '--command', 'command', required=False)
@click.option('-d', '--description', 'description', required=False)
def add(**kwargs):
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


@main.command()
def list(**kwargs):
    cmds = PrettyTable()
    cmds.field_names = ['Name', 'Command', 'Description']
    scripts = loadScripts()
    for name, data in scripts.items():
        print(data)
        row = (name, data["command"], data["description"])
        cmds.add_row(row)
    cmds.align = 'l'
    print(cmds)


@main.command()
@click.option('-n', '--name', 'name', required=False)
def rm(**kwargs):
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to remove: ')
    removeScript(name)


@main.command()
def install(**kwargs):
    runScriptDirectly('pip install -r requirements.txt')


@main.command()
def freeze(**kwargs):
    runScriptDirectly('pip freeze > requirements.txt')


@main.command()
def build(**kwargs):
    runScript('build')


@main.command()
def start(**kwargs):
    runScript('start')


@main.command()
def deploy(**kwargs):
    runScript('deploy')


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Python Script Manager")
    main()
