import click
from .. import const
from ..basic.funcs import runScriptDirectly

@click.group()
def pip():
    pass

@pip.command(name="install")
def install_command(**kwargs):
    """Install dependencies in requirements.txt"""
    runScriptDirectly('pip install -r requirements.txt')


@pip.command(name="freeze")
def freeze_command(**kwargs):
    """Output dependencies of project"""
    runScriptDirectly('pip freeze > requirements.txt')
