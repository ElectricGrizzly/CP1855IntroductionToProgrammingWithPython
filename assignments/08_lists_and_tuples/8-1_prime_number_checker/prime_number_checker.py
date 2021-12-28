"""Determine if a number is prime and display its factors if it is not."""

from verbose_math import find_factors
from config import UPPER_LIMIT, LOWER_LIMIT
from inputs import get_user_number, get_user_character
from text import display_title, range_prompt, display_range_error, display_found_prime, again_prompt, display_factors, display_farewell

def main() -> None:
    """If a number is prime, inform user. If a number is not prime, display the numbers factors to user."""
    display_title()
    while True:
        number: int = get_user_number(range_prompt(LOWER_LIMIT, UPPER_LIMIT))
        if number <= LOWER_LIMIT or number >= UPPER_LIMIT:
            display_range_error(LOWER_LIMIT, UPPER_LIMIT)
            continue
        factors, is_prime = find_factors(number)
        if is_prime:
            display_found_prime(number)
        else:
            display_factors(factors)
        again_select: str = get_user_character(again_prompt())
        if again_select.lower() != 'y':
            break
        print()
    display_farewell()

if __name__ == '__main__':
    main()