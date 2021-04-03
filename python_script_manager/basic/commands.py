import click
from prettytable import PrettyTable
from .funcs import *
from .. import const
from ..globals import MultiCommand, runScriptDirectly


@click.group(cls=MultiCommand)
def basic():
    pass


# Initialize psm
@basic.command("init")
@click.option('-t', '--template', 'template', help="Name of template")
@click.option('--files', is_flag=True, help='Init with file structure (if supported by template)')
@click.option('--disable-oninit', 'disable_oninit', is_flag=True, help='Disable work of oninit event')
def init_command(files, **kwargs):
    """Initialize PSM in current folder"""
    template = kwargs.pop('template') or input('Which template you wanna use? (blank): ') or 'blank'
    initialize(
        template,
        disable_oninit=kwargs.pop('disable_oninit')
    )


# Run script
@basic.command("run")
@click.argument('name', required=True)
def run_command(**kwargs):
    """Run PSM script with NAME"""
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to run')
    runScript(name)


# Add script
@basic.command("add")
@click.option('-n', '--name', 'name', required=False, help="Name for new script")
@click.option('-c', '--command', 'command', required=False, help="Command that script will used for")
@click.option('-d', '--description', 'description', required=False, help="Description for new script (optional)")
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
        description = input('Enter description for script (optional): ')
    addScript(name, command, description)


# List scripts
@basic.command("list")
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


# Remove script
@basic.command("rm")
@click.option('-n', '--name', 'name', required=False, help="Name of script to remove")
def rm_command(**kwargs):
    """Remove script"""
    name = kwargs.pop('name')
    while not name:
        name = input('Enter name of script to remove: ')
    removeScript(name)


# Special Scripts
@basic.command("build")
def build_command(**kwargs):
    """Special script that will execute "psm run build" """
    runScript('build')


@basic.command("start")
def start_command(**kwargs):
    """Special script that will execute "psm run start" """
    runScript('start')


@basic.command("deploy")
def deploy_command(**kwargs):
    """Special script that will execute "psm run deploy" """
    runScriptIfExist('predeploy')
    runScript('deploy')
    runScriptIfExist('postdeploy')


@basic.command(['set:version', 'set:v'])
def set_version_command(**kwargs):
    """Set version number for your project"""
    from ..package import PSMReader
    psm = PSMReader(const.filename)
    new_version = input(f'Enter new version number ({psm.data["version"]}): ')
    old_version = psm.data["version"]
    if new_version and new_version != old_version:
        psm.data['version'] = new_version
        psm.write()
        print(f'Successfully updated version: {old_version} -> {new_version}')
    