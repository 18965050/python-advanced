# genmultiplex.py


import threading, queue
from generators_uk.genqueue import *
from generators_uk.gencat import *

def multiplex(sources):
    in_q = queue.Queue()
    consumers = []
    for s in sources:
        thr = threading.Thread(target=sendto_queue,
                               args=(s,in_q))
        thr.start()
        consumers.append(genfrom_queue(in_q))
    return gen_cat(consumers)

if __name__ == '__main__':
    from generators_uk import follow
    foo_log = follow.follow(open("www/foo/access-log"))
    bar_log = follow.follow(open("www/bar/access-log"))
    for line in multiplex([foo_log,bar_log]):
        print(line)
    
