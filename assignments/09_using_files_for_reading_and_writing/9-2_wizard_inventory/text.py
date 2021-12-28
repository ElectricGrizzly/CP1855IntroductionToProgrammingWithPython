"""Text and prints used by wizard inventory program."""

COMMAND_PROMPT: str = 'Command: '

def display_title() -> None:
    """Display the title of the program."""
    print('The Wizard Inventory Program\n')

def display_farewell() -> None:
    """Display a farewell message."""
    print('\nBye!')

def display_menu() -> None:
    """Display program menu options."""
    print('COMMAND MENU')
    print('walk - Walk down the path')
    print('show - Show all items')
    print('drop - Drop an item')
    print('exit - Exit program')
    print()

def display_invalid_command(command: str) -> None:
    """Display a message indicating the input command is invalid."""
    print(f'"{command}" is not a valid command.')