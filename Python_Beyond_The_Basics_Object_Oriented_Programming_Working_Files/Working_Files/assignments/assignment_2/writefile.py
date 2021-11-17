#import abc
class WriteFile(object):

    @staticmethod
    def write(file,data):
        with open(file,'a') as file_obj:
            file_obj.write(data)


class DelimFile(WriteFile):

    def __init__(self,file,delimiter):
        self.delimiter = delimiter
        self.file = file

    #
    # def write(self,data):
    #     string_to_write =f'{self.delimiter}'.join(data) + '\n'
    #     with open(self.file,'a') as file:
    #         file.write(string_to_write)

    def write(self,data):
        string_to_write =f'{self.delimiter}'.join(data) + '\n'
        super(DelimFile,self).write(self.file,string_to_write)


# class LogFile(WriteFile):
#     import datetime as dt
#
#     def __init__(self,file):
#         self.file = file
#
#     # def write(self,msg):
#     #     now = dt.datetime.now()
#     #     timestamp = now.strftime("%d-%m-%Y %H:%M")
#     #     string_to_write ='\t'.join([timestamp, msg,'\n'])
#     #     with open(self.file,'a') as file:
#     #         file.write(string_to_write)
#
#     def write(self,msg):
#         now = dt.datetime.now()
#         timestamp = now.strftime("%d-%m-%Y %H:%M")
#         string_to_write ='\t'.join([timestamp, msg,'\n'])
#         super.write(string_to_write)



#test code

mydelim = DelimFile('data.csv',',')
mydelim.write(['a','b','c','d',])

log = LogFile('log.txt')
log.write('this is a log')
log.write('this is another  log')