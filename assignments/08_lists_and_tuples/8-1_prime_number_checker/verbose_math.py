"""Math for finding factors and checking primality of a number."""

from math import sqrt
from typing import Union

def find_factors(number: int) -> tuple[list[int], bool]:
    """Returns the factors of a number as a list and a boolean indicating if the number is prime or not."""
    factors: list[int] = [1]
    if number == 1:
        return factors
    elif number == 0:
        return [0].extend(factors)
    maximum: int = int(sqrt(number))
    integer: int = 2
    while integer <= maximum:
        if number % integer == 0:
            if integer == number // integer:
                factors.append(integer)
            else:
                factors.extend([integer, number // integer])
        integer += 1
    factors.sort()
    factors.append(number)
    if len(factors) <= 2:
        return factors, True
    return factors, False

def is_prime(number: int) -> bool:
    """Returns true if integer has only 2 factors (is prime)."""
    factors: list[int] = find_factors(number)
    if len(factors) <= 2:
        return True
    return False