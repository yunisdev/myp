import json
from typing import NoReturn, List
from .. import const


class PSMReader:
    data: dict
    file_name: str

    def __init__(self, file_name: str = const.filename):
        with open(file_name) as f:
            data: dict = json.load(f)
        self.data = data
        self.file_name = file_name

    def write(self) -> None:
        with open(self.file_name, 'wt') as f:
            json.dump(self.data, f, indent=4, sort_keys=True)

    def get_version(self) -> str:
        return self.data['version']

    def get_name(self) -> str:
        return self.data["name"]

    def get_description(self) -> str:
        return self.data["description"]

    def get_author(self) -> str:
        return self.data["author"]

    def get_author_email(self) -> str:
        return self.data["author_email"]

    def get_url(self) -> str:
        return self.data["url"]

    def get_config(self) -> str:
        return self.data.get("config", None)

    def get_use_environment(self) -> bool:
        return self.data.get("use_environment", None)

    def get_environment(self) -> str:
        return self.data.get("environment", None)

    def set_environment(self, data: str) -> None:
        self.data["environment"] = data

    def set_use_environment(self, data: bool) -> None:
        self.data["use_environment"] = data

    def set_config(self, data) -> None:
        self.data["config"] = data

    def add_script(self, name: str, command: str, description: str) -> str:
        self.data["scripts"][name] = {
            "command": command,
            "description": description,
        }
        return self.data["scripts"][name]

    def remove_script(self, name: str) -> str:
        return self.data["scripts"].pop(name)

    def add_dependency(self, package_name: List[str], scope: str = "common"):
        self.data["dependencies"][scope].extend(package_name)
        self.data["dependencies"][scope] = list(
            set(self.data["dependencies"][scope]))

    def get_dependencies(self, scope: str = "all") -> List[str]:
        deps:dict = self.data["dependencies"]
        if scope == "all":
            return list(set(deps["dev"]+deps["prod"]+deps["common"]))
        elif scope == "prod":
            return list(set(deps["prod"]+deps["common"]))
        elif scope == "dev":
            return list(set(deps["dev"]+deps["common"]))
        
        return []