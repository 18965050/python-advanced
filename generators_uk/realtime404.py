# realtime404.py
#
# Print all 404 requests as they happen in the log

from generators_uk.apachelog import *
from generators_uk.follow import *

logfile  = open("www/foo/access-log")
loglines = follow(logfile)
log      = apache_log(loglines)

r404 = (r for r in log if r['status'] == 404)

for r in r404:
    print(r['host'], r['datetime'], r['request'])
