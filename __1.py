__author__ = 'Nafiul Islam'
__title = 'Multiples of 3 and 5'


if __name__ == '__main__':

    print(sum(i for i in range(0, 1000) if not i % 3 or not i % 5))