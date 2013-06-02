__author__ = 'Nafiul Islam'
__title__ = 'Smallest Multiple'


def main(begin, end):
    list_of_numbers = range(begin, end+1)
    divisors = []
    true_flags = 0

    i = 2
    while i <= end:
        for number in list_of_numbers:
            if number % i == 0:
                true_flags += 1
        if true_flags >= 2:
            divisors.append(i)
            for index in xrange(len(list_of_numbers)):
                if list_of_numbers[index] % i == 0:
                    list_of_numbers[index] /= i
        else:
            i += 1
        true_flags = 0

    print list_of_numbers
    print divisors

    max_number = 1

    for number in list_of_numbers:
        max_number *= number

    print max_number

    for div in divisors:
        max_number *= div

    print max_number

if __name__ == "__main__":
    main(1, 20)