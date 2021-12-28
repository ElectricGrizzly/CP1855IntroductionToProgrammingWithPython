"""Manage inventory for a wizard by dropping, adding, editing, and showing items in the inventory."""

from commands import show_items, grab_item, edit_item, drop_item
from config import STARTER_ITEMS
from text import display_title, display_invalid_command, display_farewell, display_menu, COMMAND_PROMPT

def main() -> None:
    """Perform the selected Wizard Inventory function."""
    display_title()
    display_menu()
    wizard_inventory: list[str] = STARTER_ITEMS
    while True:
        command: str = input(COMMAND_PROMPT)
        if command == 'show':
            show_items(wizard_inventory)
        elif command == 'grab':
            grab_item(wizard_inventory)
        elif command == 'edit':
            edit_item(wizard_inventory)
        elif command == 'drop':
            drop_item(wizard_inventory)
        else:
            if command == 'exit':
                break
            display_invalid_command(command)
        print()
    display_farewell()

if __name__ == '__main__':
    main()