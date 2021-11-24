# import abc
#inheritance example
import datetime as dt
class WriteFile(object):

    # @staticmethod
    def write(self):
        return


class DelimFile(WriteFile):
    def __init__(self,file,delimiter):
        self.delimiter = delimiter
        self.file = file

    def write(self,data):
        string_to_write = f'{self.delimiter}'.join(data) + '\n'
        with open(self.file,'a') as file:
            file.write(string_to_write)


class LogFile(WriteFile):


    def __init__(self,file):
        self.file = file

    def write(self,msg):
        now = dt.datetime.now()
        timestamp = now.strftime("%d-%m-%Y %H:%M")
        string_to_write = '\t'.join([timestamp,msg,'\n'])
        with open(self.file,'a') as file:
            file.write(string_to_write)


# test code


mydelim = DelimFile('data.csv',',')

mydelim.write(['a','b','c','d',])

log = LogFile('log.txt')
log.write('this is a log')
log.write('this is another  log')
