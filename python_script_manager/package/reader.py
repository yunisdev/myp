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

    def get_name(self):
        return self.data["name"]

    def get_description(self):
        return self.data["description"]

    def get_author(self):
        return self.data["author"]

    def get_author_email(self):
        return self.data["author_email"]

    def get_url(self):
        return self.data["url"]

    def add_script(self,name,command,description):
        self.data["scripts"][name] = {
            "command":command,
            "description":description,
        }
        return self.data["scripts"][name]

    def remove_script(self,name):
        return self.data["scripts"].pop(name)