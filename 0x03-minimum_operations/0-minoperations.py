#!/usr/bin/python3
import math


def minOperations(n):
    """ Calculates the fewest number of operations needed to result in
        exactly n H characters.

        Args:
            @n: integer

        Return:
            the fewest number of operations needed to result in n H characters
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
