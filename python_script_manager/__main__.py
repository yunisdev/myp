import sys
import click

from .basic import basic
from .pip import pip
from .environment import environment

commands = [
    basic, 
    pip,
    environment
]

main = click.CommandCollection(sources=commands)

def cli():
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Python Script Manager")
    try:
        main()
    except Exception as e:
        print("❌ "+str(e))
