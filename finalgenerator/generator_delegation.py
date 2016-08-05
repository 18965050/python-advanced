"""
(1) yield/yield from只能放在函数/方法内
(2) yield from 可直接作用在iterator对象上
(3) generator对象创建后,可直接通过generator.send(None)触发
(4) 否则, 必须要先调用next(generator)方法
(5) yield from 作为generator代理者,会将send传入的值传送给内层generator
(6) yield from 的返回值为内层generator的返回值
(7) 协程的返回值是作为StopIteration的value返回的. 因此外层的generator代理(yield from)最好放在一个无限循环中, 屏蔽对StopIteration的默认处理
"""


def chain(x, y):
    yield from x  # (1), (2)
    yield from y


def accumulate():
    tally = 0
    while 1:
        next = yield
        if next is None:
            return tally
        tally += next


def gather_tallies(tallies):
    while 1:            #(7)  while循环屏蔽了异常的处理
        tally = yield from accumulate()  # (5),(6)
        tallies.append(tally)


if __name__ == '__main__':
    # 测试1
    a = [1, 2, 3]
    b = [4, 5, 6]
    for x in chain(a, b):
        print(x, end=' ')

    c = [7, 8, 9]
    for x in chain(a, chain(b, c)):
        print(x, end=' ')

    print()

    tallies = []

    # 测试二, 直接对协程测试
    gen=accumulate()
    next(gen)
    for i in range(4):
        gen.send(i)

    try:
        gen.send(None)
    except StopIteration as e:
        print(e.value)      #(7)


    acc = gather_tallies(tallies)
    # acc.send(None)        #(3)
    next(acc)  # (4)
    for i in range(4):
        acc.send(i)

    print(tallies)


    acc.send(None)


    print(tallies)

    for i in range(5):
        acc.send(i)

    acc.send(None)

    print(tallies)
