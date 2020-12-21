import json
import os

def loadScripts():
    with open('pyscripts.json', 'rt') as s:
        return json.load(s)['scripts']


def addScript(name, command):
    with open('pyscripts.json', 'rt') as s:
        data = json.load(s)
    with open('pyscripts.json', 'wt') as s:
        data['scripts'][name] = command
        json.dump(data, s)
    print('Script added successfully.')


def initialize():
    with open('pyscripts.json', 'wt') as s:
        data = {
            "scripts": {
                "hello": "echo Hello World!!!"
            }
        }
        json.dump(data, s)
    print('Successfully initialized py-scripts')

def removeScript(name):
    with open('pyscripts.json', 'rt') as s:
        data = json.load(s)
    with open('pyscripts.json', 'wt') as s:
        data['scripts'].pop(name)
        json.dump(data, s)
    print('Script removed successfully.')

def runScript(name):
    scripts = loadScripts()
    called_script = scripts.get(name, None)
    if called_script:
        os.system(called_script)
    else:
        raise Exception(f'Can not find script named "{name}"')