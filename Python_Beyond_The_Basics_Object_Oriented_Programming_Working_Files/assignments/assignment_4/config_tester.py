import configdict as cfd
import os
# file = 'pat'
file = r'.\config_dict.txt'
cd = cfd.ConfigDict(file)
print(type(cd))
print(cd['a'])
# print(cd['f'])
cd['f']=11

print(cd['h'])