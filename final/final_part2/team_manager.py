"""Main module for baseball team manager program"""

from cli import display_splash
from operations import run_option, read_players_from_file
from inputs import get_option
from config import players_file

def main():
    """Main function of baseball team manager program"""
    display_splash()
    players = read_players_from_file(players_file)
    while True:
        option = get_option('Menu option: ')
        run_option(option, players, players_file)
        print()

if __name__ == "__main__":
    main()