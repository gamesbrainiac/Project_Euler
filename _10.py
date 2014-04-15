import time

__author__ = 'Nafiul Islam'
__title__ = 'Summation of primes'


# Very slow implementation for some reason
# Modelled after the sieve of Eratosthenes

def main(limit=1000):
    # Because range() goes to limit-1
    limitn = limit+1

    # Creates a list, False means the index is a prime.
    not_prime = [False] * limitn

    # Creates a list to append indexes that are primes
    # primes = []

    # total for total sum
    total = 0

    # Looping over all the values up to limitn from 2
    for i in range(2, limitn):
        # If index is a prime number, then skip all else
        if not_prime[i]:
            continue
        # If index is not a prime number
        # Change all multiples of that number,
        # starting from its double to True,
        for f in range(i*2, limitn, i):
            # meaning making them not primes
            not_prime[f] = True

        # primes.append(i)
        total += i

    # Prints total
    print('== Total ==')
    print(total)

if __name__ == "__main__":
    start_time = time.time()
    main(1000000,)
    print(time.time() - start_time, "seconds")
