import sys
import click

from .basic import basic
from .pip import pip

commands = [
    basic, 
    pip
]


main = click.CommandCollection(sources=commands)

if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Python Script Manager")
    main()
