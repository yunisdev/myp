from . import const
import json
import os
import subprocess
import click
from .package import MYPReader
from termcolor2 import c
from PyInquirer import prompt
from typing import Any, List


def loadScripts() -> dict:
    myp = MYPReader()
    return myp.get_data("scripts")


def runScriptDirectly(script: str):
    click.echo('\n\t' + c('>').blue + c('>').yellow + f' {script}\n')
    myp_obj: MYPReader = MYPReader()
    output: subprocess.CompletedProcess
    if myp_obj.get_data("use_environment"):
        # os.system(f'snakenv {myp_obj.get_data("environment")} -c "{script}"')
        output = subprocess.run(['pipenv','run', *script.split()])
    else:
        # os.system(script)
        output = subprocess.run(script.split())
    if not output.returncode == 0:
        raise Exception(f"Process exited with code {output.returncode}")

def runScriptIfExist(name: str):
    scripts = loadScripts()
    called_script = scripts.get(name, None)
    if called_script:
        cmd = called_script["command"]
        runScriptDirectly(cmd)
    else:
        pass


def runScript(name: str, unknown_options: dict = {}):
    scripts = loadScripts()
    called_script = scripts.get(name, None)
    if called_script:
        cmd = called_script["command"]
        runScriptDirectly(cmd.format(**unknown_options))
    else:
        raise click.ClickException(f'Can not find script named "{name}"')


def take_input(text):
    questions = [
        {
            'type': 'input',
            'name': 'data',
            'message': text
        }
    ]

    answers = prompt(questions)
    return answers['data']


def process_unknown_options(args: List[str]) -> dict:
    data: dict = {}
    temp: str = ""
    for arg in args:
        if arg.startswith("--"):
            key, value = arg[2:].split("=")
            data[key] = value
        elif arg.startswith("-"):
            temp = arg[1:]
        else:
            if temp != "":
                data[temp] = arg
                temp = ""
    return data


def pip_cmd(cmd: str) -> str:
    import sys
    return f"python -m pip {cmd}"


def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line.split('==')[0] for line in lineiter if line and not line.startswith("#")]
