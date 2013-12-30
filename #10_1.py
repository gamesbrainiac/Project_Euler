import time

__author__ = 'Nafiul Islam'
__title__ = 'Summation of primes'

# Very slow implementation, may take you 30 seconds


def main(*args):
    list_primes = [2]
    total = 2
    number = 3
    loop = 0  # performance check

    while number < args[0]:
        for val in list_primes:
            if number % val == 0:
                break
            elif number % val != 0 and val == list_primes[-1]:
                list_primes.append(number)
                total += number
        number += 1
        loop += 1
        if loop % 100:
            print('@ Loop:', loop, list_primes[-1], '||', 'Difference:', loop - list_primes[-1])
            pass

    print(' == Total == ')
    print(total)

if __name__ == "__main__":
    start_time = time.time()
    main(100000,)
    print(time.time() - start_time, "seconds")