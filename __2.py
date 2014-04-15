__author__ = 'Nafiul Islam'
__title = 'Even Fibonacci numbers'


def fibonacci(start=1):
    a, b = start, start
    yield start
    while True:
        _ret = a + b
        a, b = b, _ret
        yield _ret

if __name__ == '__main__':

    total = 0
    for i in fibonacci():
        if i < 4*10**6 and not i % 2:
            total += i
        elif i > 4*10**6:
            break

    print(total)