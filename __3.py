__author__ = 'Nafiul Islam'
__title__ = 'Largest prime factor'

number_in_question = 600851475143


def largest_prime_factor(number_in_question):
    """Finds the largest prime factor for the given number
    
    Args:
        number_in_question
       
    Returns:
        largest_prime_factor
    """
    
    divisor = 2
    factors = []

    while number_in_question > 1:
        if number_in_question % divisor == 0:
            factors.append(divisor)
            number_in_question /= divisor
        else:
            divisor += 1

    print("Factors were:")
    print(factors)
    return max(factors)


if __name__ == "__main__":
    print("The largest factor: "+ str(largest_prime_factor(600851475143)))