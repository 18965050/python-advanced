def receiver():
    while True:
        item = yield
        print('Got', item)


if __name__ == '__main__':
    recv = receiver()
    next(recv)  # Advance to first yield
    recv.send('Hello')
    recv.send('World')
