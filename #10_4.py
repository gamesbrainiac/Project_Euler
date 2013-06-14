import time

__author__ = 'Nafiul Islam'
__title__ = 'Summation of primes'


# Very slow implementation for some reason
# Modelled after the sieve of Eratosthenes

def main(limit=1000):
    limitn = limit+1  # To account for 0
    not_prime = [False] * limitn
    primes = []

    total = 0
    for i in xrange(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)
        total += i

    print '== Total =='
    print total

if __name__ == "__main__":
    start_time = time.time()
    main(1000000,)
    print time.time() - start_time, "seconds"
