import json

class PSMReader:
    def __init__(self,file_name):
        with open(file_name) as f:
            data = json.load(f)
        self.data = data
        self.file_name = file_name
    def write(self):
        with open(self.file_name,'wt') as f:
            json.dump(self.data,f)
    
    def get_version(self):
        return self.data['version']