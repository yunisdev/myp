# <img src="https://raw.githubusercontent.com/YunisDEV/python-script-manager/master/assets/psm.svg"/> Welcome to PSM

## What is PSM?

<b>PSM</b> (Python Script Manager) is a <b>script manager</b> for Python programming language. You can manage your scripts with this tool. You can create scripts, use them, delete them and etc. PSM gives you chance to call longer commands with shorter commands. I inspired by <b>npm scripts</b> to make Python version of it.
Check out <a href="https://yunisdev.github.io/python-script-manager/FEATURES.html">New features</a> or <a href="https://yunisdev.github.io/python-script-manager/CONTRIBUTION.html">Contribution</a> documentation

# Installation

For install PSM you will need pip. I you have not click <a href="https://pip.pypa.io/en/stable/">here</a>
After installing pip, enter command below.

```bash
pip3 install python-script-manager
```

To make sure you have successfully installed it,

```bash
psm
```

# Usage

First you need to initialize PSM in your directory.

```bash
psm init
```

You can also start with template.

#### Available templates:

-   blank
-   django
-   flaskmng
-   pypi

Example,

```bash
psm init -t django
# or
psm init --template="django"
```

It will create `psm.json` which keeps your script informations.

## Create Script

To create script, use `add` command.

```bash
psm add
```

It will ask you name, command and description (optional) for your script.
You can also pass them as options

```bash
psm add --name="Name of script" --command="Command" --description="Description for script (optional)"
```

## List scripts

To get list of scripts, enter command below:

```bash
psm list
```

## Run scripts

To run scripts use syntax below:

```bash
psm run [SCRIPT_NAME]
```

## Remove script

If you want to remove unused scripts, enter command below:

```bash
psm rm -n [SCRIPT_NAME]
```

## Special scripts

If you name a script which is in list below, you can use special script feature.

#### List of special scripts:

-   start
-   deploy
-   build

To run special scripts, use syntaxt below:

```bash
psm SPECIAL_SCRIPT
```

Example,

```bash
psm build
```

## PIP shortcuts

To install dependencies in `requirements.txt`, use

```bash
psm install
```

Or you can output dependencies to `requirements.txt`

```bash
psm freeze
```

## Project settings
#### Setting version
Optionally, you can define version for your project. If you are building python package, it is useful for versioning.
To set new version:
```bash
psm setv
# or
psm set-version
```
It will not change, if you do not enter any value to input.
To use version in `setup.py` for your packages, you can use `PSMReader` object.
```python
from python_script_manager.package import PSMReader

psm = PSMReader('directory of psm.json')
# in most cases, "psm.json" will work as directory

setuptools.setup(
    # ...
    version=psm.get_version(),
    # ...
```
