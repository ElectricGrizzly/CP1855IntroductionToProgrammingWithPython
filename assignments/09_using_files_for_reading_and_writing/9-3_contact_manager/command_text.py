"""Text entities and CLI displays for commands of contact manager program."""

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

NUMBER_PROMPT = 'Number: '
NAME_PROMPT = 'Name: '
EMAIL_PROMPT = 'Email: '
PHONE_PROMPT = 'Phone: '