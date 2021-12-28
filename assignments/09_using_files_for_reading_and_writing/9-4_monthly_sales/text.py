"""Text and CLI entities ofd monthly sales program."""

def display_title() -> None:
    """Display the program title."""
    print('Monthly Sales program\n')

def display_menu() -> None:
    """Display program menu options."""
    print('COMMAND MENU')
    print('monthly - View monthly sales')
    print('yearly - View yearly summary')
    print('edit - Edit sales for a month')
    print('exit - Exit program')
    print()

def display_invalid_command(command: str) -> None:
    """Display a message indicating the input command is invalid."""
    print(f'"{command}" is not a valid command.')

def display_farewell() -> None:
    """Display a farewell message."""
    print('Bye!')

COMMAND_PROMPT = 'Command: '