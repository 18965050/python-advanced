# gencat.py
#
# Concatenate multiple generators into a single sequence

def gen_cat(sources):
    for s in sources:
        for item in s:
            if isinstance(item,str):    # line有可能是bytes类型, 这种情况下后续处理有问题(比如正则等), 因此过滤之
                yield item

# Example use

if __name__ == '__main__':
    from generators_uk.genfind import  gen_find
    from generators_uk.genopen import  gen_open

    lognames = gen_find("access-log*","www")
    logfiles = gen_open(lognames)
    loglines = gen_cat(logfiles)
    for line in loglines:
        print(line, end=' ')
