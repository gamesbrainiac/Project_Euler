__author__ = 'Nafiul Islam'
__title = 'Even Fibonacci numbers'


def fibonacci(num=0):
    NUM_ZERO = 1
    NUM_ONE = 2

    if num == 0:
        return NUM_ZERO
    if num == 1:
        return NUM_ONE
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

if __name__ == "__main__":
    sumOfNumbers = 0
    var = 0

    while fibonacci(var) < 4 * (10 ** 6):
        if fibonacci(var) % 2 == 0:
            sumOfNumbers += fibonacci(var)
        var += 1

    print(sumOfNumbers)