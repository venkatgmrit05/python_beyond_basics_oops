class ConfigDict(dict):

    def __init__(self,
                 file):
        self.file = file
        self.read_config_file()

    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        self.write_to_config_file(key,value)


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


con_file = r'.\config_dict.txt'
cd = ConfigDict(con_file)
print(cd)


