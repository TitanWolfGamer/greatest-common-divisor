def gcd(a: int, b: int) -> int:
    """
    gcd stands for "Greatest Common Divisor" and can compute that using the euclidian algorithm
    :param a: The first number
    :param b: The second number
    :return: The Greatest Common Divisor of these two numbers
    """
    remainder = a % b
    while remainder:
        a = b
        b = remainder
        remainder = a % b
    return b
