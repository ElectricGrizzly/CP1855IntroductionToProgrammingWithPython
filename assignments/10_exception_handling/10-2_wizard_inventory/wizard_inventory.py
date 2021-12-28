"""Main module of the wizard inventory program."""

from commands import show_items, drop_item, walk, give_starter_items, confirm_all_items_file
from text import display_title, display_invalid_command, display_farewell, display_menu, COMMAND_PROMPT

def main() -> None:
    """Main function for the wizard inventory program."""
    display_title()
    confirm_all_items_file()
    display_menu()
    wizard_inventory: list[str] = give_starter_items()
    while True:
        command: str = input(COMMAND_PROMPT)
        if command == 'show':
            show_items(wizard_inventory)
        elif command == 'drop':
            drop_item(wizard_inventory)
        elif command == 'walk':
            walk(wizard_inventory)
        else:
            if command == 'exit':
                break
            display_invalid_command(command)
        print()
    display_farewell()

if __name__ == '__main__':
    main()