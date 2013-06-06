__author__ = 'Nafiul Islam'
__title__ = 'Summation of primes'


# Faster but still slow

def main(*argv):
    list_of_numbers = range(3, argv[0], 2)

    for n in list_of_numbers:
        list_to_remove = [n * i for i in list_of_numbers[:argv[0]/n-1]]
        for r in list_to_remove:
            try:
                list_of_numbers.remove(r)
            except ValueError:
                pass

    list_of_numbers = [2] + list_of_numbers

    total = 0
    for var in list_of_numbers:
        total += var
    print ''
    print '== Total =='
    print total
    # print list_of_numbers

if __name__ == "__main__":
    main(2000000,)