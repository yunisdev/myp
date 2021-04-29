from ..package import PSMReader

def addScript(name: str, command: str, description: str = ""):
    psm = PSMReader()
    psm.add_script(
        name=name,
        command=command,
        description=description,
    )
    psm.write()
    print('Script added successfully.')


def removeScript(name: str):
    psm = PSMReader()
    psm.remove_script(name)
    psm.write()
    print('Script removed successfully.')
