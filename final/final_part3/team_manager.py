"""Baseball team manager program."""

from cli import display_splash, display_menu
from operations import run_option, read_players_from_file
from inputs import get_option
from config import players_file

def main():
    """Perform the selection team manager function."""
    display_splash()
    players = read_players_from_file(players_file)
    while True:
        try:
            option = get_option('Menu option: ')
            run_option(option, players, players_file)
        except ValueError:
            print('Not a valid option. Please try again')
            print()
            display_menu()
            continue
        print()

if __name__ == '__main__':
    main()