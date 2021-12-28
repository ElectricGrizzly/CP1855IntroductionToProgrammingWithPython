"""Text entities and CLI displays for contact manager program."""

def display_title() -> None:
    """Display the program title."""
    print('Contact Manager\n')

def display_menu() -> None:
    """Display program menu options."""
    print('COMMAND MENU')
    print('list - Display all contacts')
    print('view - View a contact')
    print('add - Add a contact')
    print('del - Delete a contact')
    print('exit - Exit program')
    print()

def display_invalid_command(command: str) -> None:
    """Display a message indicating the input command is invalid."""
    print(f'"{command}" is not a valid command.')
    
def display_farewell() -> None:
    """Display a farewell message."""
    print('Bye!')

COMMAND_PROMPT = 'Command: '