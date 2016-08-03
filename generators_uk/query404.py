# query404.py
#
# Find the set of all documents that 404 in a log file

from generators_uk.linesdir import *
from generators_uk.apachelog import *

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

stat404 = set(r['request'] for r in log
              if r['status'] == 404)

for r in sorted(stat404):
    print(r)
