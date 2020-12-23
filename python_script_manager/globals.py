from . import const
import json
import os


def loadScripts():
    with open(const.filename, 'rt') as s:
        return json.load(s)['scripts']


def runScriptDirectly(script):
    print(f'\n\t> {script}\n')
    os.system(script)
