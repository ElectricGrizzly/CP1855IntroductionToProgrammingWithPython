"""Baseball team manager program."""

from cli import display_splash
from operations import run_option
from inputs import get_option
from config import players

def main() -> None:
    """Perform the selection team manager function."""
    display_splash()
    while True:
        option = get_option('Menu option: ')
        run_option(option, players)
        print()

if __name__ == '__main__':
    main()