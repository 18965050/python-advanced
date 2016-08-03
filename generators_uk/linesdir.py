# linesdir.py
#
# Generate a sequence of lines from files in a directory

from generators_uk.genfind import *
from generators_uk.gencat import *
from generators_uk.genopen import *

def lines_from_dir(filepat, dirname):
    names = gen_find(filepat,dirname)
    files = gen_open(names)
    lines = gen_cat(files)
    return lines

# Example use

if __name__ == '__main__':
    loglines = lines_from_dir("access-log*","www")
    for line in loglines:
        print(line, end=' ')
