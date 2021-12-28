"""User input for baseball team manager program."""

from cli_entities import MENU_OPTIONS, POSITIONS

def get_option(prompt: str, options: list[str] = MENU_OPTIONS) -> int:
    """Gets an option from the user and ensures it's valid."""
    while True:
        option: int = int(input(prompt))
        if option > 0 and option <= len(options):
            return option
        else:
            raise ValueError('Not a valid option. Please try again.')

def get_position(prompt: str) -> str:
    """Gets a position from the user and ensures it's valid."""
    try:
        while True:
            position: str = input(prompt)
            if position.upper() not in POSITIONS:
                raise ValueError('Not a valid position.')
            else:
                return position
    except ValueError as exception:
        print(exception)
        return get_position(prompt)

def get_lineup_number(prompt: str, lineup: list[list[str]]) -> int:
    """Gets a lineup number from the user and ensures it's valid."""
    while True:
        lineup_number: int = get_int(prompt)
        if lineup_number <= 0 or lineup_number > len(lineup):
            print(f"Invalid lineup number.")
        else:
            return lineup_number

def get_int(prompt: str) -> str:
    """Gets an integer from the user and ensures it's valid."""
    try:
        while True:
            integer: int = int(input(prompt))
            if integer >= 0 and integer <= 10000:
                return integer
            else:
                print("Invalid integer. Must be from 0 to 10,000.")
    except ValueError:
        print('Must be a valid integer!')
        return get_int(prompt)

def get_string(prompt: str) -> str:
    """Gets a string from the user."""
    while True:
        return input(prompt)

