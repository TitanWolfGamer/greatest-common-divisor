def gcd(a: int, b: int) -> int:
    """
    gcd stands for "Greatest Common Divisor" and can compute that using the Euclidean algorithm
    :param a: the first number
    :param b: The second number
    :return: the greatest common divisor of the two given numbers
    """
    r: int = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


# example usage
def example() -> None:
    num_a: int = int(input('Enter divisor: '))
    num_b: int = int(input('Enter dividend: '))

    gcd_of_ab: int = gcd(num_a, num_b)
    print(f'GCD of both numbers: {gcd_of_ab}')

    print(f'Your Input: {num_a}/{num_b}')
    print(f'Your simplified input: {num_a // gcd_of_ab}/{num_b // gcd_of_ab}')
    print(f'= {num_a / num_b}')

if __name__ == '__main__':
    example()
