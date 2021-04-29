import os
import json
import click
from .. import const
from ..templates import templates


def initialize(template_name, disable_oninit=False):
    template = templates[template_name]
    schema = template['body']
    schema["version"] = '0.0.0'
    schema["config"] = {}
    schema["dependencies"] = {"prod": [], "common": [], "dev": []}
    schema["environment"] = ""
    schema["use_environment"] = True
    current_dir = os.path.basename(os.getcwd())

    # Get inputs
    schema["name"] = click.prompt('Enter project name', default=current_dir)
    schema["description"] = click.prompt('Enter decription', default="")
    schema["author"] = click.prompt('Enter author name', default="")
    schema["author_email"] = click.prompt('Enter author email', default="")
    schema["url"] = click.prompt('Enter url', default="")

    oninit = template.get('oninit', None)
    if oninit and not disable_oninit:
        oninit()
    with open(const.filename, 'wt') as s:
        json.dump(schema, s, indent=4, sort_keys=True)
    click.echo('Successfully initialized ' +
               const.filename+f' with {template_name} template.')
