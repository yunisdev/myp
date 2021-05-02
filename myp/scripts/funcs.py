from ..package import MYPReader

def addScript(name: str, command: str, description: str = ""):
    myp = MYPReader()
    myp.add_script(
        name=name,
        command=command,
        description=description,
    )
    myp.write()
    print('Script added successfully.')


def removeScript(name: str):
    myp = MYPReader()
    myp.remove_script(name)
    myp.write()
    print('Script removed successfully.')
