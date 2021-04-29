import sys
import click

@click.group()
def main():
    pass

from .basis import *
from .scripts import *
from .pip import *
from .get import *

def cli():
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Python Script Manager")
    try:
        main()
    except Exception as e:
        print("❌ "+str(e))
