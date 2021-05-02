from ..__main__ import main
from ..globals import runScriptDirectly, pip_cmd


@main.command("install")
def install_command():
    """Install dependencies in requirements.txt"""
    runScriptDirectly(pip_cmd(f"install -r requirements.txt"))


@main.command("freeze")
def freeze_command():
    """Output dependencies of project to requirements.txt"""
    runScriptDirectly(pip_cmd(f"freeze > requirements.txt"))
