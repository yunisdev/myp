import os
import sys
import click
import json

def loadScripts():
    with open('pyscripts.json','rt') as s:
        return json.load(s)['scripts']

def addScript(name,command):
    with open('pyscripts.json','rt') as s:
        data = json.load(s)
    with open('pyscripts.json','wt') as s:
        data['scripts'][name] = command
        json.dump(data,s) 
    print('Script added successfully.')

@click.group()
@click.version_option("0.0.1")
def main():
    pass

@main.command()
@click.argument('name',required=True)
def run(**kwargs):
    script_name = kwargs.pop('name')
    scripts = loadScripts()
    called_script = scripts.get(script_name,None)
    if called_script:
        os.system(called_script)
    else:
        raise Exception(f'Can not find script named "{script_name}"')

@main.command()
@click.option('-n','--name','name',required=True)
@click.option('-c','--command','command',required=True)
def add(**kwargs):
    name = kwargs.pop('name')
    command = kwargs.pop('command')
    addScript(name,command)


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("py-scripts")
    main()