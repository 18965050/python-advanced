def countdown(n):
    while n > 0:
        yield n
        n -= 1

if __name__=='__main__':
    for x in countdown(10):
        print('T-minus', x)

    c = countdown(3)
    next(c)
    next(c)
    c.__next__()
    # next(c)
    # next(c)