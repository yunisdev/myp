import click
from .. import const
from ..basic.funcs import runScriptDirectly

@click.group()
def pip():
    pass

@pip.command()
def install(**kwargs):
    """Install dependencies in requirements.txt"""
    runScriptDirectly('pip install -r requirements.txt')


@pip.command()
def freeze(**kwargs):
    """Output dependencies of project"""
    runScriptDirectly('pip freeze > requirements.txt')
