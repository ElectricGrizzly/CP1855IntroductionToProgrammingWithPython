"""Contact manager program."""

from commands import list_contacts, view_contact, add_contact, delete_contact, read_contacts
from text import display_title, display_menu, display_invalid_command, display_farewell, COMMAND_PROMPT

def main():
    """Perform the selected contact manager function."""
    display_title()
    display_menu()
    contacts: list[list[str]] = read_contacts()
    while True:
        command: str = input(COMMAND_PROMPT)
        if command == 'list':
            list_contacts(contacts)
        elif command == 'view':
            view_contact(contacts)
        elif command == 'add':
            add_contact(contacts)
        elif command == 'del':
            delete_contact(contacts)
        else:
            if command == 'exit':
                break
            display_invalid_command(command)
        print()
    display_farewell()

if __name__ == '__main__':
    main()