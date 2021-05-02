import click
from .funcs import (
    initialize
)
from ..package import MYPReader
from ..__main__ import main


# Initialize MYP
@main.command("init")
@click.option('-t', '--template', 'template', help="Name of template", prompt='Which template you wanna use?', default='blank')
@click.option('--disable-oninit', 'disable_oninit', is_flag=True, help="Disable work of oninit event")
def init_command(template, disable_oninit, **kwargs):
    """Initialize MYP in current folder"""
    initialize(
        template,
        disable_oninit=disable_oninit
    )


# Set command
@main.command("set")
@click.argument('name', required=True)
@click.option('-v', '--value', 'value', required=False,help="Value to assing to key")
def set_command(name, value):
    """Set value of key in myp.json"""
    myp:MYPReader = MYPReader()
    new_value = value or input(f'Enter new {name} [{myp.get_data(name)}]: ')
    old_value = myp.get_data(name)
    if new_value and new_value != old_value:
        myp.set_data(name, new_value)
        myp.write()
        click.echo(f'Successfully updated {name}: {old_value} -> {new_value}')


# Show command
@main.command("show")
@click.argument('name', required=True)
def get_commmand(name):
    """Show value of key in myp.json"""
    myp:MYPReader = MYPReader()
    click.echo(myp.get_data(name))
