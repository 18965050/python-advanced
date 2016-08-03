# storelast.py
#
# An iterator that stores the last value returned.  

class storelast(object):
    def __init__(self,source):
        self.source = source
    def __next__(self):
        item = next(self.source)
        self.last = item
        return item
    def __iter__(self):
        return self

# Example
if __name__ == '__main__':
    from generators_uk.follow import *
    from generators_uk.apachelog import *

    lines = storelast(follow(open("www/foo/access-log")))
    log   = apache_log(lines)

    for r in log:
        print(r)
        print(lines.last)
