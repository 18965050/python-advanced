# bytesgen.py
#
# An example of chaining together different generators into a processing
# pipeline.    

from generators_uk.genfind import *
from generators_uk.genopen import *
from generators_uk.gencat import *
from generators_uk.gengrep import *

pat    = r'ply-.*\.gz'
logdir = 'www'

filenames = gen_find("access-log*",logdir)
logfiles  = gen_open(filenames)
loglines  = gen_cat(logfiles)
patlines  = gen_grep(pat,loglines)
bytecol   = (line.rsplit(None,1)[1] for line in patlines)
bytes     = (int(x) for x in bytecol if x != '-')

print("Total", sum(bytes))

