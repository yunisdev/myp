import click
from typing import List
from ..package import PSMReader
from ..globals import runScriptDirectly, pip_cmd, parse_requirements
from ..__main__ import main


@main.command("get")
@click.option('--dev', required=False, is_flag=True, help="Get packages as development dependency")
@click.option('--prod', required=False, is_flag=True, help="Get packages as development dependency")
@click.argument('package_names', required=True, nargs=-1)
def get_command(dev: bool, prod: bool, package_names: List[str]) -> None:
    """Get packages"""
    psm: PSMReader = PSMReader()
    package_scope: str = "common" if dev+prod != 1 else ("prod" if prod else "dev")
    psm.add_dependency(package_names, package_scope)
    runScriptDirectly(pip_cmd(f"install {' '.join(package_names)}"))
    psm.write()


@main.command("get:deps")
@click.option('--dev', required=False, is_flag=True, help="Get packages as development dependency")
@click.option('--prod', required=False, is_flag=True, help="Get packages as development dependency")
def get_deps_command(dev: bool, prod: bool) -> None:
    """Get packages in psm.json"""
    psm: PSMReader = PSMReader()
    deps: List[str] = psm.get_dependencies(
        "dev" if dev else ("prod" if prod else "all"))
    runScriptDirectly(pip_cmd(f"install {' '.join(deps)}"))


@main.command("get:load-from")
@click.option('--dev', required=False, is_flag=True, help="Get packages as development dependency")
@click.option('--prod', required=False, is_flag=True, help="Get packages as development dependency")
@click.argument('file_name', default='requirements.txt')
def get_load_from_reqs_command(dev: bool, prod: bool, file_name: str) -> None:
    """Get dependencies in requirements file"""
    psm: PSMReader = PSMReader()
    reqs: List[str] = parse_requirements(file_name)
    reqs_scope: str = "common" if dev+prod != 1 else ("prod" if prod else "dev")
    psm.add_dependency(reqs, reqs_scope)
    runScriptDirectly(pip_cmd(f"install {' '.join(reqs)}"))
    psm.write()
