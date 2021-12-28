"""This file provides the operations and display for team manager program"""

from .team_manager_cli_entities import HORIZONTAL_DIVIDER, INVALID_OPTION, MAIN_TITLE, OPTION_MESSAGE, OPTIONS, PROMPTS, DIVIDER_LENGTH
from .baseball_stats import batting_average

def menu_selection():
    """Used to navigate control sequence based on user selection"""
    while True:
        option = get_integer_option(OPTION_MESSAGE["title"])
        if option == 1:
            calculate_batting_average()
        elif option == 2:
            break
        else:
            print(INVALID_OPTION + "\n")
            display_options(divider=False)
            return menu_selection()
    print(OPTION_MESSAGE["option_2"])

def calculate_batting_average():
    """Calculates the batting average and provides prompts for required input"""
    print(OPTION_MESSAGE["option_1"])
    at_bats = get_integer_option(PROMPTS["at_bats"])
    hits = get_integer_option(PROMPTS["hits"])
    print("Batting average:", batting_average(at_bats, hits), "\n")

def display_header():
    """Display the header in CLI"""
    print(DIVIDER_LENGTH*HORIZONTAL_DIVIDER)
    print(int((DIVIDER_LENGTH-len(MAIN_TITLE))/2)*" " + MAIN_TITLE)

def get_integer_option(prompt):
    """Prompts the user with $prompt and returns the users input as an integer"""
    return int(input(prompt))

def display_options(divider=True):
    """Display menu options in CLI"""
    print(OPTIONS["title"])
    print(OPTIONS["option_1"])
    print(OPTIONS["option_2"])
    if divider: print(DIVIDER_LENGTH*HORIZONTAL_DIVIDER)
    else: print()

def start_team_manager():
    """Used to deploy and start the team manager program"""
    display_header()
    display_options()
    menu_selection()