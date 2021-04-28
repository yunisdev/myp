import click
from ..basic.funcs import runScriptDirectly
from ..globals import MultiCommand
from ..package import PSMReader
from typing import List
from ..globals import take_input
input = take_input


@click.group(cls=MultiCommand)
def get():
    pass


@get.command("get")
@click.option('--dev', required=False, is_flag=True)
@click.option('--prod', required=False, is_flag=True)
@click.argument('package_names', required=True, nargs=-1)
def get_command(dev: bool, prod: bool, package_names: List[str]) -> None:
    psm: PSMReader = PSMReader()
    package_scope: str = "common"
    if dev+prod < 2:
        package_scope = "dev" if dev else "prod"
    psm.add_dependency(package_names, package_scope)
    runScriptDirectly(f'pip install {" ".join(package_names)}')
    psm.write()


@get.command("get:deps")
@click.option('--dev', required=False, is_flag=True)
@click.option('--prod', required=False, is_flag=True)
def get_deps_command(dev: bool, prod: bool) -> None:
    psm: PSMReader = PSMReader()
    deps: List[str] = psm.get_dependencies(
        "dev" if dev else ("prod" if prod else "all"))
    runScriptDirectly(f"pip install {' '.join(deps)}")


@get.command("get:load-from")
@click.option('--dev', required=False, is_flag=True)
@click.option('--prod', required=False, is_flag=True)
@click.argument('file_name', default='requirements.txt')
def get_load_from_reqs_command(dev: bool, prod: bool, file_name: str) -> None:
    psm: PSMReader = PSMReader()
    def parse_requirements(filename):
        lineiter = (line.strip() for line in open(filename))
        return [line.split('==')[0] for line in lineiter if line and not line.startswith("#")]
    reqs = parse_requirements(file_name)
    reqs_scope = "common"
    if dev+prod < 2:
        reqs_scope = "dev" if dev else "prod"
    psm.add_dependency(reqs, reqs_scope)
    runScriptDirectly(f"pip install {' '.join(reqs)}")
