"""Contact manager command functions."""

from csv import reader, writer
from command_text import display_contact_error, display_contact_info, display_added, display_deleted, NUMBER_PROMPT, NAME_PROMPT, EMAIL_PROMPT, PHONE_PROMPT 

def read_contacts() -> list[list[str]]:
    """Read contacts from contacts file."""
    with open('contacts.csv', encoding='utf-8') as contacts_csv:
        csv = reader(contacts_csv)
        return [row for row in csv]

def _save_to_csv(contacts: list[list[str]]) -> None:
    """Save the contacts to contacts file."""
    with open('contacts.csv', 'w', newline='', encoding='utf-8') as contacts_csv:
        csv = writer(contacts_csv)
        csv.writerows(contacts)

def list_contacts(contacts: list[list[str]]) -> None:
    """List the contacts in the contact list."""
    for index, contact in enumerate(contacts):
        print(f'{index + 1}. {contact[0]}')
    
def view_contact(contacts: list[list[str]]) -> None:
    """View the contact information of a contact."""
    contact_number: int = int(input(NUMBER_PROMPT))
    if not _is_contact_number(contact_number, contacts):
        display_contact_error(contact_number)
    else:
        contact = contacts[contact_number - 1]
        display_contact_info(contact)

def add_contact(contacts: list[list[str]]) -> None:
    """Add a contact to the contact list."""
    name: str = input(NAME_PROMPT)
    email: str = input(EMAIL_PROMPT)
    phone: str = input(PHONE_PROMPT)
    contact: list[str] = [name, email, phone]
    contacts.append(contact)
    _save_to_csv(contacts)
    display_added(contact)

def delete_contact(contacts: list[list[str]]) -> None:
    """Delete a contact from the contact list."""
    contact_number: int = int(input(NUMBER_PROMPT))
    if not _is_contact_number(contact_number, contacts):
        display_contact_error(contact_number)
    else:
        contact: list[str] = contacts.pop(contact_number - 1)
        _save_to_csv(contacts)
        display_deleted(contact)

def _is_contact_number(contact_number: int, contacts: list[list[str]]) -> bool:
    """Private method to determine if the given contact number is a valid contact number."""
    return False if contact_number > len(contacts) or contact_number < 1 else True