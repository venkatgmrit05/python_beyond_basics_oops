# import abc
#composition example
import datetime as dt


class WriteFile(object):

    def __init__(self,
                 file,
                 writer_class):
        self.file = file
        self.writer_class = writer_class()

    def write(self,data):
        with open(self.file,'a') as fh:
            fh.write(self.writer_class.format(data))


class csv_formatter(object):
    def __init__(self):
        self.delimiter = ','

    def format(self,data):
        string_to_write = self.delimiter.join(data) + '\n'
        return string_to_write


class log_formatter(object):
    def __init__(self):
        now = dt.datetime.now()
        self.timestamp = now.strftime("%d-%m-%Y %H:%M")
        self.delimiter = '\t'

    def format(self,data):
        string_to_write = self.delimiter.join([self.timestamp,
                                               data,'\n'])
        return string_to_write


# test code 2:
file = 'csv_data_ec.csv'
data_to_csv = ['a','1','b','2']
# csv_data = csv_formatter(file)
writer = WriteFile(file,csv_formatter)
writer.write(data_to_csv)


data_to_log = 'aa edo bokkale'
writer = WriteFile(file,log_formatter)
writer.write(data_to_log)