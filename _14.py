# encoding=utf-8

__title__ = 'Longest Collatz Sequence'
__author__ = 'Quazi Nafiul Islam'

CACHE = {1: 1}


def num_collatz(n):
    _n = n
    total = 1
    while True:
        if n in CACHE:
            total += CACHE[n]
            CACHE[_n] = total
            return total
        if not n % 2:
            n //= 2
        elif n % 2:
            if n == 1:
                break
            n = (3 * n) + 1
        total += 1
    return total

m = 1
for i in range(13, 10**6, 2):
    if num_collatz(i) > m:
        m = num_collatz(i)
        print(i, m)