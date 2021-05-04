import click
from typing import List
from ..package import MYPReader
from ..globals import runScriptDirectly, pip_cmd, parse_requirements
from ..__main__ import main


@main.command("get")
@click.option('--dev', required=False, is_flag=True, help="Get packages as development dependency")
@click.option('--prod', required=False, is_flag=True, help="Get packages as production dependency")
@click.argument('package_names', required=True, nargs=-1)
def get_command(dev: bool, prod: bool, package_names: List[str]) -> None:
    """Get packages"""
    myp: MYPReader = MYPReader()
    package_scope: str = "common" if dev+prod != 1 else ("prod" if prod else "dev")
    myp.add_dependency(package_names, package_scope)
    runScriptDirectly(pip_cmd(f"install {' '.join(package_names)}"))
    myp.write()


@main.command("get:deps")
@click.option('--dev', required=False, is_flag=True, help="Get development dependencies")
@click.option('--prod', required=False, is_flag=True, help="Get production dependencies")
def get_deps_command(dev: bool, prod: bool) -> None:
    """Get packages in myp.json"""
    myp: MYPReader = MYPReader()
    deps: List[str] = myp.get_dependencies(
        "dev" if dev else ("prod" if prod else "all"))
    runScriptDirectly(pip_cmd(f"install {' '.join(deps)}"))


@main.command("get:load-from")
@click.option('--dev', required=False, is_flag=True, help="Load packages as development dependency")
@click.option('--prod', required=False, is_flag=True, help="Load packages as production dependency")
@click.argument('file_name', default='requirements.txt')
def get_load_from_reqs_command(dev: bool, prod: bool, file_name: str) -> None:
    """Get dependencies in requirements file"""
    myp: MYPReader = MYPReader()
    reqs: List[str] = parse_requirements(file_name)
    reqs_scope: str = "common" if dev+prod != 1 else ("prod" if prod else "dev")
    myp.add_dependency(reqs, reqs_scope)
    runScriptDirectly(pip_cmd(f"install {' '.join(reqs)}"))
    myp.write()


@main.command("get:update")
@click.argument('package_names', required=True, nargs=-1)
def get_update_command(package_names) -> None:
    runScriptDirectly(pip_cmd(f"install --upgrade {' '.join(package_names)}"))


@main.command("get:remove")
@click.argument('package_names', required=True, nargs=-1)
def get_remove_command(package_names) -> None:
    myp: MYPReader = MYPReader()
    runScriptDirectly(pip_cmd(f"uninstall {' '.join(package_names)}"))
    dependencies = myp.get_data('dependencies')
    new_deps = {"dev": [], "prod": [], "common": []}
    for scope in ["dev", "prod", "commmon"]:
        for dep in dependencies[scope]:
            if not dep in package_names:
                new_deps[scope].append(dep)
    myp.set_data('dependencies', new_deps)
