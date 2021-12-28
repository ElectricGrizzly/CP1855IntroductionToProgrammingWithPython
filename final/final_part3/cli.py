"""Module for CLI functions for baseball team manager program."""

from cli_entities import (
    FAREWELL, LINEUP_AT_BATS_LENGTH, LINEUP_AT_BATS_TITLE, LINEUP_AVERAGE_LENGTH, LINEUP_AVERAGE_TITLE, LINEUP_DIVIDER, 
    LINEUP_HITS_LENGTH, LINEUP_HITS_TITLE, LINEUP_NUMBER_LENGTH, LINEUP_NUMBER_TITLE, LINEUP_PLAYER_LENGTH, LINEUP_PLAYER_TITLE, 
    LINEUP_POSITION_LENGTH, LINEUP_POSITION_TITLE, PROGRAM_TITLE, HORIZONTAL_DIVIDER, CONSOLE_LENGTH, MENU_TITLE, MENU_OPTIONS, 
    POSITION_TITLE, POSITIONS
    )

def display_divider(separator: str = HORIZONTAL_DIVIDER, length: int = CONSOLE_LENGTH) -> None:
    """Displays a horizonal divider for CLI of separaters repeated length times."""
    print(separator*length)

def display_title(title: str = PROGRAM_TITLE, length: int = CONSOLE_LENGTH) -> None:
    """Display the program title in the center of CLI window."""
    print((length - len(title))//2*' ' + title)

def display_menu(menu_heading: str = MENU_TITLE, options: list[str] = MENU_OPTIONS) -> None:
    """Display the options menu for program."""
    print(menu_heading)
    for index, option in enumerate(options):
        print(f'{index + 1} - {option}')
    print()

def display_positions(position_heading: str = POSITION_TITLE, positions: list[str] = POSITIONS):
    """Displays the possible positions for the baseball team."""
    print(position_heading)
    print(', '.join(positions))

def display_splash(
        separator: str = HORIZONTAL_DIVIDER, length: int = CONSOLE_LENGTH, title: str = PROGRAM_TITLE, menu_heading: str = MENU_TITLE, 
        options: list[str] = MENU_OPTIONS, position_heading: str = POSITION_TITLE, positions: list[str] = POSITIONS
        ) -> None:
    """Display the splash screen composing of dividers, program title, options menu, and available positions."""
    display_divider(separator, length)
    display_title(title, length)
    display_menu(menu_heading, options)
    display_positions(position_heading, positions)
    display_divider(separator, length)

def display_farewell() -> None:
    """Display a farewell message on program exit."""
    print(FAREWELL)

def display_lineup_header(
        number_heading: str = LINEUP_NUMBER_TITLE, number_length: int = LINEUP_NUMBER_LENGTH, player_heading: str = LINEUP_PLAYER_TITLE, 
        player_length: int = LINEUP_PLAYER_LENGTH, position_heading: str = LINEUP_POSITION_TITLE, position_length: int = LINEUP_POSITION_LENGTH, 
        at_bats_heading: str = LINEUP_AT_BATS_TITLE, at_bats_length: int = LINEUP_AT_BATS_LENGTH, hits_heading: str = LINEUP_HITS_TITLE, 
        hits_length: int = LINEUP_HITS_LENGTH, average_heading: str = LINEUP_AVERAGE_TITLE, average_length: int = LINEUP_AVERAGE_LENGTH, 
        seperator: str = LINEUP_DIVIDER
        ) -> None:
    """Display the table header for team lineup."""
    number_heading += (number_length - len(number_heading))*' '
    player_heading += (player_length - len(player_heading))*' '
    position_heading += (position_length - len(position_heading))*' '
    at_bats_heading += (at_bats_length - len(at_bats_heading))*' '
    hits_heading += (hits_length - len(hits_heading))*' '
    average_heading += (average_length - len(average_heading))*' '
    print(number_heading + player_heading + position_heading + at_bats_heading + hits_heading + average_heading)
    print(seperator*(number_length + player_length + position_length + at_bats_length + hits_length + average_length))

def display_player(
        lineup_number: int, player: list[str], number_length: int = LINEUP_NUMBER_LENGTH, player_length: int = LINEUP_PLAYER_LENGTH, 
        position_length: int = LINEUP_POSITION_LENGTH, at_bats_length: int = LINEUP_AT_BATS_LENGTH, hits_length: int = LINEUP_HITS_LENGTH, 
        average_length: int = LINEUP_AVERAGE_LENGTH
        ) -> None:
    """Display the player in tabulated form for team lineup"""
    number_column = f'{lineup_number}' + (number_length - len(str(lineup_number)))*' '
    player_column = f'{player[0]}' + (player_length - len(player[0]))*' '
    position_column = f'{player[1]}' + (position_length - len(player[1]))*' '
    at_bats_column = f'{player[2]}' + (at_bats_length - len(str(player[2])))*' '
    hits_column = f'{player[3]}' + (hits_length - len(str(player[3])))*' '
    average_column = f'{player[4]}' + (average_length - len(str(player[4])))*' '
    print(number_column + player_column + position_column + at_bats_column + hits_column + average_column)

def display_player_stats(player: list[str]) -> None:
    """Display statistics of selected player"""
    print(f'You selected {player[0]} AB={player[2]} H={player[3]}')

def display_player_position(player: list[str]) -> None:
    """Display position of selected player"""
    print(f'You selected {player[0]} POS={player[1]}')

def display_player_updated(player: list[str]) -> None:
    """Display which player was updated"""
    print(f'{player[0]} was updated.')