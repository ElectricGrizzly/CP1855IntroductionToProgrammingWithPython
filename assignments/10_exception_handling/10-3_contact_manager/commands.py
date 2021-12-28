"""Contact manager command functions."""

from csv import reader, writer
from command_text import display_contact_info, display_added, display_deleted, NUMBER_PROMPT, NAME_PROMPT, EMAIL_PROMPT, PHONE_PROMPT 

def read_contacts(file: str) -> None:
    """Read contacts from file. Create a new contacts file if one doesn't exist."""
    try:
        with open(file, encoding='utf-8') as contacts_csv:
            csv = reader(contacts_csv)
            return [row for row in csv]
    except FileNotFoundError:
        print('Could not find contacts file!')
        print('Starting new contacts file...')
        print()
        _save_to_csv(file, contacts=[])

def _save_to_csv(file: str, contacts: list[list[str]]) -> None:
    """Private function to save file to CSV."""
    with open(file, 'w', newline='', encoding='utf-8') as contacts_csv:
        csv = writer(contacts_csv)
        csv.writerows(contacts)

def list_contacts(contacts: list[list[str]]) -> None:
    """List the contacts in the contact list."""
    if contacts:
        for index, contact in enumerate(contacts):
            print(f'{index + 1}. {contact[0]}')
    else:
        print('There are no contacts in the list.')
    
def view_contact(contacts: list[list[str]]) -> None:
    """View the contact information of a contact."""
    try:
        contact_number: int = int(input(NUMBER_PROMPT))
    except ValueError:
        print('Invalid integer.')
        return
    try:
        contact = contacts[contact_number - 1]
        display_contact_info(contact)  
    except IndexError:
        print('Invalid contact number.')

def add_contact(contacts: list[list[str]], file: str) -> None:
    """Add a contact to the contact list."""
    name: str = input(NAME_PROMPT)
    email: str = input(EMAIL_PROMPT)
    phone: str = input(PHONE_PROMPT)
    contact: list[str] = [name, email, phone]
    contacts.append(contact)
    _save_to_csv(file, contacts)
    display_added(contact)

def delete_contact(contacts: list[list[str]], file: str) -> None:
    """Delete a contact from the contact list."""
    try:
        contact_number: int = int(input(NUMBER_PROMPT))
    except ValueError:
        print('Invalid integer.')
        return
    try:
        contact: list[str] = contacts.pop(contact_number - 1)
        _save_to_csv(file, contacts)
        display_deleted(contact)
    except IndexError:
        print('Invalid contact number.')