import sys

def doubleit(x):
    var = x*3
    return var

if __name__=='__main__':
    input_val =  sys.argv[1]
    doubled_val = doubleit(input_val)