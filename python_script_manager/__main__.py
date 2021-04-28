import sys
import click

from .basic import basic
from .pip import pip
from .environment import environment
from .get import get

commands = [
    basic, 
    pip,
    environment,
    get
]

main = click.CommandCollection(sources=commands) # type: ignore

def cli():
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Python Script Manager")
    try:
        main()
    except Exception as e:
        print("❌ "+str(e))
