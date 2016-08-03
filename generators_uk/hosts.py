# hosts.py
#
# Find unique host IP addresses

from generators_uk.linesdir import *
from generators_uk.apachelog import *

lines = lines_from_dir("access-log*", "www")
log = apache_log(lines)

hosts = set(r['host'] for r in log)
for h in hosts:
    print(h)
