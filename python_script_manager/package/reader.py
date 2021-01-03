import json
from .. import const

class PSMReader:
    def __init__(self,file_name=const.filename):
        with open(file_name) as f:
            data = json.load(f)
        self.data = data
        self.file_name = file_name
    def write(self):
        with open(self.file_name,'wt') as f:
            json.dump(self.data,f)
    
    def get_version(self):
        return self.data['version']

    def add_script(self,name,command,description):
        self.data["scripts"][name] = {
            "command":command,
            "description":description,
        }
        return self.data["scripts"][name]

    def remove_script(self,name):
        return self.data["scripts"].pop(name)