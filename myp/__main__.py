import sys
import click

@click.group()
def main():
    pass

from .basis import *
from .scripts import *
from .pip import *

def cli():
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("ManageYourPython")
    try:
        main()
    except Exception as e:
        print("❌ [MYP] "+str(e))
        exit(1)
