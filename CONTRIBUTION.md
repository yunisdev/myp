## Want to contribute PSM?
#### What you can do?
- [Create new template for `init`](#create-template)
- [Create new useful commands](#create-commands)

### Create template
For adding new template, go to `python_script_manager/templates` and create file with your template name (Example, `template.py`). After create dict with same name as template name.
Example,
```python
template = {
    "scripts":{
        "start":{
           "command":"START_COMMAND",
           "description":"Start server"
        }
    }
}
```
Don't forget to register your template to `__init__.py`
```python
from .template import template

templates = {
    # ...,
    "template":template
}

```

### Create commands
To create new commands, create new folder in `python_script_manager` folder named in your command group. For example, `hello`. After, create 3 files inside it. `__init__.py`, `commands.py` and `funcs.py`.
In `commands.py`, create new group and commands.
Example,
```python
import click
from .. import const
from ..basic.funcs import runScriptDirectly

@click.group()
def hello():
    pass

@hello.command()
def world(**kwargs):
    """Description"""
    # ...
```
To learn more about adding commands, read [Click docs](https://click.palletsprojects.com/)
In `funcs.py` add optional functions or other stuff. Because adding it to `commands.py` will make code more complex. But for constant values, like default filename or version, add it to `python_script_manager/const.py` then import it to anywhere you need. After finishing commands, import it to `__init__.py`. Example,
```python
# __init__.py
from .commands import hello
```
And also import it to `python_script_manager/__main__.py` and add to `commands` list:
```python
import sys
import click

# old command imports
from .hello import hello

commands = [
    # old commands...,
    hello
]


main = click.CommandCollection(sources=commands)


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Python Script Manager")
    main()

```
After send pull request with notes of what you did.

**Thank you!**