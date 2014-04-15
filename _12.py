__author__ = "Quazi Nafiul Islam"
__title__ = 'Highly Divisible Triangular Number'

from itertools import count, combinations, cycle
from operator import mul
from functools import reduce


def triangles():
    for i in count(1):
        yield (i * (i + 1)) // 2


# Perhaps, if cache was added, this would be faster
def divisors(n):
    l = [1]

    for i in count(2):
        for _ in cycle([i]):
            if not n % i:
                n //= i
                l.append(i)
            else:
                break
        if n == 1:
            break

    return len(set([reduce(mul, pair)
                    for sets in [combinations(l, n) for n in range(2, len(l))]
                    for pair in sets])) + 1


if __name__ == '__main__':

    for t in triangles():
        if divisors(t) > 500:
            print(t, divisors(t))
            break