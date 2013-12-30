import time

__author__ = 'Nafiul Islam'
__title__ = 'Summation of primes'


# Very slow implementation for some reason
# Modelled after the sieve of Eratosthenes

def main(*args):
    list_of_numbers = range(3, args[0], 2)

    for n in list_of_numbers:
        list_to_remove = [n * i for i in list_of_numbers[:args[0]/n-1]]
        for r in list_to_remove:
            try:
                list_of_numbers.remove(r)  # Possibly expensive
            except ValueError:
                pass

    list_of_numbers = [2] + list_of_numbers

    total = 0
    for var in list_of_numbers:
        total += var
    print('== Total ==')
    print(total)
    # print list_of_numbers

if __name__ == "__main__":
    start_time = time.time()
    main(100000,)
    print(time.time() - start_time, "seconds")

# Results
# == Total ==
# 454396537
# 4.23399996758 seconds
