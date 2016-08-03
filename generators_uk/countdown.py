class countdown:

    def __init__(self,start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):         # 注意: python2中, override next()方法
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

def countdown2(n):
    print('Counting down from',n)
    while n > 0:
        yield n
        n -= 1

if __name__=='__main__':
    for x in countdown(10):
        print(x, end=',')

    print()

    gen=countdown2(10)
    gen.__next__()
    for x in gen:
        print(x, end=',')