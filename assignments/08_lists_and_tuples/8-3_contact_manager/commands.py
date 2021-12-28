"""Contact manager command functions."""

from text import display_contact_error, display_contact_info, display_added, display_deleted, NUMBER_PROMPT, NAME_PROMPT, EMAIL_PROMPT, PHONE_PROMPT 

def list_contacts(contacts: list[list[str]]) -> None:
    """List the contacts in the contact list."""
    for index, contact in enumerate(contacts):
        print(f'{index + 1}. {contact[0]}')
    
def view_contact(contacts: list[list[str]]) -> None:
    """View the contact information of a contact."""
    contact_number: int = int(input(NUMBER_PROMPT))
    if contact_number > len(contacts) or contact_number < 1:
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
    display_added(contact)

def delete_contact(contacts: list[list[str]]) -> None:
    """Delete a contact from the contact list."""
    contact_number: int = int(input(NUMBER_PROMPT))
    if contact_number > len(contacts) or contact_number < 1:
        display_contact_error(contact_number)
    else:
        contact: list[str] = contacts.pop(contact_number-1)
        display_deleted(contact)