"""User input for baseball team manager program."""

from cli_entities import MENU_OPTIONS, POSITIONS

def get_option(prompt: str, options: list[str] = MENU_OPTIONS) -> int:
    """Gets an option from the user and ensures it's valid."""
    while True:
        option: int = int(input(prompt))
        if option > 0 and option <= len(options):
            return option
        else:
            print("Invalid option!")

def get_position(prompt: str) -> str:
    """Gets a position from the user and ensures it's valid."""
    while True:
        position: str = input(prompt)
        if position not in POSITIONS:
            print(f"Invalid position. Must be one of {POSITIONS}")
        else:
            return position

def get_lineup_number(prompt: str, lineup: list[list[str]]) -> int:
    """Gets a lineup number from the user and ensures it's valid."""
    while True:
        lineup_number: int = int(input(prompt))
        if lineup_number <= 0 or lineup_number > len(lineup):
            print(f"Invalid lineup number.")
        else:
            return lineup_number

def get_int(prompt: str) -> str:
    """Gets an integer from the user and ensures it's valid."""
    while True:
        integer: int = int(input(prompt))
        if integer >= 0 and integer <= 10000:
            return integer
        else:
            print("Invalid integer. Must be from 0 to 10,000.")

def get_string(prompt: str) -> str:
    """Gets a string from the user."""
    while True:
        return input(prompt)

