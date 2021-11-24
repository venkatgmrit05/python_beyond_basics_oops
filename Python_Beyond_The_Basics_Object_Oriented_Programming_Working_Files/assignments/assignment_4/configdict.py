import os


class ConfigKeyError(Exception):
    def __init__(self,
                 *args):
        print('calling my err')
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        print('the raised expetion is my error class')
        if self.message:
            print('error message is {}'.format(self.message))
            return self.message
        else:
            print('no message')


class ConfigDict(dict):

    def __init__(self,file):

        try:
            print(os.path.isfile(file))
            self.file = file
            self.read_config_file()
        except Exception as e:
            print(e)

    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        self.write_to_config_file(key,value)

    def __getitem__(self,key):
        try:
            return dict.__getitem__(self,key)
        except ConfigKeyError as e:
            print(e)

    def read_config_file(self):
        with open(self.file,'r') as fh:
            data = fh.readlines()
        for line in data:
            key,val = line.split('=')
            val = val.strip()
            self[key] = val

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
