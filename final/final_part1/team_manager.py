"""Main module for baseball team manager program"""

from cli import display_splash
from operations import run_option
from inputs import get_option
from config import players

def main():
    """Main function of baseball team manager program"""
    display_splash()
    while True:
        option = get_option('Menu option: ')
        run_option(option, players)
        print()

if __name__ == "__main__":
    main()