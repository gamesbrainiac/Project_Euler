__author__ = 'Nafiul Islam'
__title__ = 'Special Pythagorean triplet'


def main(argv):
    for c in range(1, argv+1):
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c == argv:
                    # print a, b, c
                    if a**2 + b**2 == c**2:
                        print('a =', a, 'b =', b, 'c =', c)
                        print('a^2 =', a**2)
                        print('b^2 =', b**2)
                        print('a^2 + b^2 =', a**2 + b**2)
                        print('c^2 =', c**2)
                        print('a * b * c =', a*b*c)

if __name__ == "__main__":
    main(1000)