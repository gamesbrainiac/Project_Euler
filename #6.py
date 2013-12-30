__author__ = 'Nafiul Islam'
__title__ = 'Sum square difference'

import math


def main(argv):
    sum_of_squares = 0
    sum_squared = 0

    # Getting the sum of individual squares
    for i in range(1, argv + 1):
        sum_of_squares += i ** 2

    # Getting total sum of numbers squared
    for i in range(1, argv + 1):
        sum_squared += i

    sum_squared **= 2

    print("Sum of the squares:", sum_of_squares)
    print("Sum squared:", sum_squared)
    print(math.fabs(sum_of_squares - sum_squared))


if __name__ == "__main__":
    main(100)