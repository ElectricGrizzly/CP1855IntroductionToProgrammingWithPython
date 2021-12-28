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

def display_contact_error(contact_number: int) -> None:
    """Display error when incorrect contact number used."""
    print(f'There is no contact {contact_number}')

def display_contact_info(contact: list[str]) -> None:
    """Display the contact info of a contact."""
    print(f'Name: {contact[0]}')
    print(f'Email: {contact[1]}')
    print(f'Phone: {contact[2]}')

def display_deleted(contact: list[str]) -> None:
    """Display the deleted contact."""
    print(f'{contact[0]} was deleted.')

def display_added(contact: list[str]) -> None:
    """Display the added contact."""
    print(f'{contact[0]} was added.')

COMMAND_PROMPT = 'Command: '
NUMBER_PROMPT = 'Number: '
NAME_PROMPT = 'Name: '
EMAIL_PROMPT = 'Email: '
PHONE_PROMPT = 'Phone: '