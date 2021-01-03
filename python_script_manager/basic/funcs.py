import json

from .. import const
from ..templates import templates

from ..globals import *

def addScript(name, command, description=""):
    with open(const.filename, 'rt') as s:
        data = json.load(s)
    with open(const.filename, 'wt') as s:
        data['scripts'][name] = {
            "command": command, "description": description}
        json.dump(data, s)
    print('Script added successfully.')


def initialize(template_name,disable_oninit = False):
    template = templates[template_name]
    schema = template['body']
    schema["version"] = '0.0.0'
    oninit = template.get('oninit',None)
    if oninit and not disable_oninit:
        oninit()
    with open(const.filename, 'wt') as s:
        json.dump(schema, s)
    print('Successfully initialized ' +
          const.filename+f' with {template_name} template.')


def removeScript(name):
    with open(const.filename, 'rt') as s:
        data = json.load(s)
    with open(const.filename, 'wt') as s:
        data['scripts'].pop(name)
        json.dump(data, s)
    print('Script removed successfully.')

