import pytest
import configdict
import os
file = r'.\config_dict.txt'

def test_read_config_file():
    # assert isinstance(self.file, os.path.isfile)
    assert type(configdict.ConfigDict(file) == configdict.ConfigDict

#
# def test_write_to_config_file(self):
#     assert False


# test_read_config_file(file)