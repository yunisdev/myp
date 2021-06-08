import json
from typing import List, Any
from .. import const
from pipfile import Pipfile

class MYPReader:
    data: dict
    file_name: str

    def __init__(self, file_name: str = const.filename):
        with open(file_name) as f:
            data: dict = json.load(f)
        self.data = data
        self.file_name = file_name

    def write(self) -> None:
        """Write object instance to `myp.json`"""
        with open(self.file_name, 'wt') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)

    def get_data(self, key: str) -> Any:
        """Get data from object"""
        return self.data[key]

    def set_data(self, key: str, value: Any) -> None:
        """Set data to object"""
        self.data[key] = value

    def add_script(self, name: str, command: str, description: str) -> str:
        """Add script to object"""
        self.data["scripts"][name] = {
            "command": command,
            "description": description,
        }
        return self.data["scripts"][name]

    def remove_script(self, name: str) -> str:
        """Remove script from object"""
        return self.data["scripts"].pop(name)

    def get_dependencies(self, scope: str = "default") -> List[str]:
        """Get dependencies of object"""
        deps: dict = Pipfile.load(filename="./Pipfile").data
        if scope == "default":
            return list(deps["default"]) 
        elif scope == "dev":
            return list(deps["develop"])
        return []
