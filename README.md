# Welcome to PSM <img width="30px" src="assets/psm.svg"></img>
### What is PSM?
<b>PSM</b> (Python Script Manager) is a <b>script manager</b> for Python programming language. You can manage your scripts with this tool. You can create scripts, use them, delete them and etc. PSM gives you chance to call longer commands with shorter commands. I inspired by <b>npm scripts</b> to make Python version of it.
Check out <a href="FEATURES.md">New features</a> or <a href="CONTRIBUTION.md">Contribution</a> documentation
## Installation

For install PSM you will need pip. I you have not click <a href="https://pip.pypa.io/en/stable/">here</a>
After installing pip, enter command below.
```bash
pip3 install python-script-manager
```
To make sure you have successfully installed it,
```bash
psm --version
```

## Usage
First you need to initialize PSM in your directory.
```bash
psm init
```
It will create `psm.json` which keeps your script informations.
By default, `psm init` will add script named `hello` which output `Hello World!!!` to screen.
#### Create Script
To create script, use `add` command.
```bash
psm add
```
It will ask you name and command for your script.
You can also pass them as options
```bash
psm add --name="Name of script" --command="Command"
```
#### List scripts
To get list of scripts, enter command below:
```bash
psm list
```
#### Run scripts
To run scripts use syntax below:
```bash
psm run [SCRIPT_NAME]
```
#### Remove script
If you want to remove unused scripts, enter command below:
```bash
psm rm -n [SCRIPT_NAME]
```
#### Special scripts
If you name a script which is in list below, you can use special script feature.
###### List of special scripts:
- start
- deploy
- build

To run special scripts, use syntaxt below:
```bash
psm SPECIAL_SCRIPT
```
Example,
```bash
psm build
```

#### PIP shortcuts
To install dependencies in `requirements.txt`, use
```bash
psm install
```
Or you can output dependencies to `requirements.txt`
```bash
psm freeze
```