import json
import os
try:
    from . import const
except ImportError:
    import const

def loadScripts():
    with open(const.filename, 'rt') as s:
        return json.load(s)['scripts']


def addScript(name, command):
    with open(const.filename, 'rt') as s:
        data = json.load(s)
    with open(const.filename, 'wt') as s:
        data['scripts'][name] = command
        json.dump(data, s)
    print('Script added successfully.')


def initialize():
    with open(const.filename, 'wt') as s:
        data = {
            "scripts": {
                "hello": "echo Hello World!!!"
            }
        }
        json.dump(data, s)
    print('Successfully initialized '+const.filename)

def removeScript(name):
    with open(const.filename, 'rt') as s:
        data = json.load(s)
    with open(const.filename, 'wt') as s:
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