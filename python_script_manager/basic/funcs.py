import json
from .. import const
from ..templates import templates
from ..package import PSMReader
from ..globals import *

def addScript(name, command, description=""):
    psm = PSMReader()
    psm.add_script(
        name=name,
        command=command,
        description=description,
    )
    psm.write()
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
    psm = PSMReader()
    psm.remove_script(name)
    psm.write()
    print('Script removed successfully.')

