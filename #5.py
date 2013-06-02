__author__ = 'Nafiul Islam'
__title__ = 'Smallest Multiple'


def main():
    max_number = 1
    list_of_possibilities = []
    for number in xrange(1, 11):
        max_number *= number

    print max_number

    while max_number % 2 == 0 and max_number != 0:
        max_number /= 2
        list_of_possibilities.append(max_number)
        print max_number

    print list_of_possibilities

if __name__ == "__main__":
    main()