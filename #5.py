__author__ = 'Nafiul Islam'
__title__ = 'Smallest Multiple'


def main():
    max = 1
    true_flags = 0
    for number in xrange(1, 10):
        max *= number
    print max


if __name__ == "__main__":
    main()