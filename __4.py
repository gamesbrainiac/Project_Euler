__author__ = 'Nafiul Islam'
__title__ = 'Largest palindrome from two 3 digit numbers'

number_one = range(100, 999)
number_two = range(100, 999)


def is_palindrome(prod):
    prod = str(prod)
    length = len(prod)
    if prod[:length / 2] == prod[::-1][:length / 2]:
        return True
    return False


if __name__ == '__main__':

    largest_palindrome = 0
    pair = (0, 0)

    for one in number_one:
        for two in number_two:
            product = one * two
            if is_palindrome(product):
                if product > largest_palindrome:
                    pair = (one, two)
                    largest_palindrome = product

    print(pair)
    print(largest_palindrome)