# largest.py
#
# Find the largest file

from generators_uk.linesdir import *
from generators_uk.apachelog import *

lines = lines_from_dir("access-log*","www")
log = apache_log(lines)

print("%d %s" % max((r['bytes'],r['request'])
                    for r in log))
