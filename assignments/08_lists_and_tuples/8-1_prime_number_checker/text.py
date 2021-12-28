"""Prompts and displayed text for prime number checker program."""

def display_title() -> None:
    """Displays the programs title."""
    print("Prime Number Checker\n")

def display_farewell() -> None:
    """Displays a farewell message."""
    print("\nBye!")

def display_range_error(lower_limit: int, upper_limit: int) -> None:
    """Displays an error when user input a value outside of the set range."""
    print(f'The number must be BETWEEN {lower_limit} and {upper_limit}!\n')

def display_found_prime(prime: int) -> None:
    """Display the message when a prime is found."""
    print(f'{prime} is a prime number.')

def display_factors(factors: list) -> None:
    """Display the factors of the input number."""
    print(f'{factors[-1]} is NOT a prime number.')
    print(f'It has {len(factors)} factors: {" ".join([str(factor) for factor in factors])}')

def range_prompt(lower_limit: int, upper_limit: int) -> str:
    """Returns the prompt requesting user integer input."""
    return f'Please enter an integer between {lower_limit} and {upper_limit}: '

def again_prompt() -> str:
    """Return the prompt request user character input."""
    return f'\nTry again? (y/n): '