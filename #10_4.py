import time

__author__ = 'Nafiul Islam'
__title__ = 'Summation of primes'


# Very slow implementation for some reason
# Modelled after the sieve of Eratosthenes

def main(limit=1000):
    list_of_numbers = [True] * limit
    list_of_numbers[0] = list_of_numbers[1] = False

    total = 0
    for (i, isprime) in enumerate(list_of_numbers):
        if isprime:
            yield i
            total += i
            for n in xrange(i*i, limit, i):
                list_of_numbers[n] = False

    print '== Total =='
    print total

if __name__ == "__main__":
    start_time = time.time()
    main(100000,)
    print time.time() - start_time, "seconds"
