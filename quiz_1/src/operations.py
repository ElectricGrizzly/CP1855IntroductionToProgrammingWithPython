"""This file provides the operations and display for team manager program"""

from .team_manager_cli_entities import HORIZONTAL_DIVIDER, INVALID_OPTION, MAIN_TITLE, OPTION_MESSAGE, OPTIONS
from .baseball_stats import batting_average

def menu_selection():
    """Used to navigate control sequence based on user selection"""
    while True:
        option = int(input(OPTION_MESSAGE["title"]))
        if option == 1:
            calculate_batting_average()
        elif option == 2:
            break
        else:
            print(INVALID_OPTION + "\n")
            return menu_selection()
    print(OPTION_MESSAGE["option_2"])

def calculate_batting_average():
    """Calculates the batting average and provides prompts for required input"""
    print(OPTION_MESSAGE["option_1"])
    at_bats = int(input("Official number of at bats: "))
    hits = int(input("Number of hits: "))
    print("Batting average:", batting_average(at_bats, hits), "\n")

def display_header():
    """Display the header in CLI"""
    print(72*HORIZONTAL_DIVIDER)
    
    print(int((72-len(MAIN_TITLE))/2)*" " + MAIN_TITLE)

def display_options():
    """Display menu options in CLI"""
    print(OPTIONS["title"])
    print(OPTIONS["option_1"])
    print(OPTIONS["option_2"])
    print(72*HORIZONTAL_DIVIDER)

def start_team_manager():
    """Used to deploy and start the team manager program"""
    display_header()
    display_options()
    menu_selection()