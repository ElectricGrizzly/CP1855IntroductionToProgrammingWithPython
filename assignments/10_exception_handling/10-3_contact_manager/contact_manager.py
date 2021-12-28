"""Contact manager program."""

from commands import list_contacts, view_contact, add_contact, delete_contact, read_contacts
from text import display_title, display_menu, display_invalid_command, display_farewell, COMMAND_PROMPT
from config import CONTACT_CSV

def main():
    """Perform selected contact manager function."""
    display_title()
    display_menu()
    contacts: list[list[str]] = read_contacts(CONTACT_CSV)
    while True:
        command: str = input(COMMAND_PROMPT)
        if command == 'list':
            list_contacts(contacts)
        elif command == 'view':
            view_contact(contacts)
        elif command == 'add':
            add_contact(contacts, CONTACT_CSV)
        elif command == 'del':
            delete_contact(contacts, CONTACT_CSV)
        else:
            if command == 'exit':
                break
            display_invalid_command(command)
        print()
    display_farewell()

if __name__ == '__main__':
    main()