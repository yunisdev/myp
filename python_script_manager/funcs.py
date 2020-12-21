import json
import os
try:
    from . import const
    from .templates import templates
except ImportError:
    import const
    from templates import templates


def loadScripts():
    with open(const.filename, 'rt') as s:
        return json.load(s)['scripts']


def runScriptDirectly(script):
    print(f'\n\t> {script}\n')
    os.system(script)


def addScript(name, command,description=""):
    with open(const.filename, 'rt') as s:
        data = json.load(s)
    with open(const.filename, 'wt') as s:
        data['scripts'][name] = {"command":command,"description":description}
        json.dump(data, s)
    print('Script added successfully.')


def initialize(template):
    schema = templates[template]
    with open(const.filename, 'wt') as s:
        json.dump(schema, s)
    print('Successfully initialized '+const.filename+f' with {template} template.')


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
    cmd = called_script["command"]
    if called_script:
        print(f'\n\t> {cmd}\n')
        os.system(cmd)
    else:
        raise Exception(f'Can not find script named "{name}"')
