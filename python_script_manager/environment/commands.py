import click
from ..basic.funcs import runScriptDirectly
from ..globals import MultiCommand
from ..package import PSMReader

from ..globals import take_input
input = take_input

@click.group(cls=MultiCommand)
def environment():
    pass


@environment.command("set:env")
def set_env_command(**kwargs):
    """Set environment of project"""
    psm = PSMReader()
    old_env = psm.get_environment()
    new_env = input(
        f'Enter environment name{f" ({old_env})" if old_env else ""}: ')
    psm.set_environment(new_env)
    psm.write()
    print(f'Successfully updated environment: {old_env} -> {new_env}')


@environment.command("set:use-env")
@click.option('--activate/--deactivate',is_flag=True,default=True)
def set_use_env_command(activate,*args, **kwargs):
    """Set environment usage of project"""
    psm = PSMReader()
    psm.set_use_environment(activate)
    psm.write()
    print(
        f'Successfully {"de" if not activate else ""}activated environment usage')
