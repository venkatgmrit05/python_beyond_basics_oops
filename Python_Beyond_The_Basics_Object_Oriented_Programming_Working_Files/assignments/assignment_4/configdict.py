import os
import pysnooper




class ConfigKeyError(Exception):
    def __init__(self,this,key):
        print('initializing  CKE')
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return 'key {} not found. The available keys are  {}'.format(self.key,".".join(self.keys))


class ConfigDict(dict):

    def __init__(self,file):

        try:
            print(os.path.isfile(file))
            self.file = file
        except Exception as e:
            print(e)
        self.read_config_file()

    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        self.write_to_config_file(key,value)

    def __getitem__(self,key):
        if not key in self:
            raise ConfigKeyError(self,key)
        else:
            return dict.__getitem__(self,key)

    #@pysnooper.snoop()
    def read_config_file(self):
        try:
            with open(self.file,'r') as fh:
                data = fh.readlines()
            for line in data:
                key,val = line.split('=')
                val = val.strip()
                self[key] = val
        except Exception as e:
            print(e)

    def write_to_config_file(self,k,v):
        _data = []
        for item in self.keys():
            if item == k:
                _text = f"{item}={v}" + '\n'
            else:
                _text = f"{item}={self[item]}" + '\n'

            _data.append(_text)
        with open(self.file,'w') as fh:
            fh.writelines(_data)

