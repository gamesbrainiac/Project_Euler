__author__ = 'Nafiul Islam'
__title__ = '10001st prime'

# This is probably a very inefficient way of solving the problem, so
# if anyone reading this finds a better one, please let me know.


def main(argv):
    list_primes = [2]
    number = 3
    loop = 0  # performance check

    while len(list_primes) < argv:
        for val in list_primes:
            if number % val == 0:
                break
            elif number % val != 0 and val == list_primes[-1]:
                list_primes.append(number)
        number += 1
        loop += 1

    print('Prime @', argv, 'is', list_primes[-1])


if __name__ == "__main__":
    main(10001)