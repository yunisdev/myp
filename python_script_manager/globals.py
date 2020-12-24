from . import const
import json
import os
import click

def loadScripts():
    with open(const.filename, 'rt') as s:
        return json.load(s)['scripts']


def runScriptDirectly(script):
    print(f'\n\t> {script}\n')
    os.system(script)

class MultiCommand(click.Group):
    def command(self, *args, **kwargs):
        """Behaves the same as `click.Group.command()` except if passed
        a list of names, all after the first will be aliases for the first.
        """
        def decorator(f):
            if isinstance(args[0], list):
                _args = [args[0][0]] + list(args[1:])
                for alias in args[0][1:]:
                    cmd = super(MultiCommand, self).command(
                        alias, *args[1:], **kwargs)(f)
                    cmd.short_help = "Alias for '{}'".format(_args[0])
            else:
                _args = args
            cmd = super(MultiCommand, self).command(
                *_args, **kwargs)(f)
            return cmd
        return decorator