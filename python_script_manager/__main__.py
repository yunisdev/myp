import sys
import click

from .basic import basic
from .pip import pip


main = click.CommandCollection(sources=[basic, pip])


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Python Script Manager")
    main()
