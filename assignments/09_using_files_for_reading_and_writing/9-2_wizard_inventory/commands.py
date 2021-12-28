"""Commands of the wizard inventory program."""

from config import ITEM_LIMIT, ALL_ITEMS_FILE, STORED_ITEMS_FILE, STARTER_ITEM_NUMBER
from random import randint

def show_items(items: list[str]) -> None:
    """Show the items in the inventory."""
    for index, item in enumerate(items):
        print(f'{index + 1}. {item}')

def drop_item(items: list[str]) -> None:
    """Drop an item at the specified inventory location."""
    inventory_location: int = int(input('Number: '))
    if not _is_inventory_location(inventory_location, items):
        print(f'There is no item number {inventory_location}!')
    else:
        item = items.pop(inventory_location - 1)
        print(f'{item} was dropped')
        _save_to_file(STORED_ITEMS_FILE, items)

def walk(items: list[str]) -> None:
    """Get a random item from the all items file. If user wants item, grab the item."""
    wizard_items: list[str] = _get_items_from_file(ALL_ITEMS_FILE)
    item: str = get_random_item(wizard_items)
    print(f'While walking down a path, you see {item}')
    take_item: str = input('Do you want to grab it? (y/n): ')
    if take_item.lower() == 'y':
        _grab_item(items, item)

def _grab_item(items: list[str], item: str) -> None:
    """Private function to grab an item and add it to inventory if there is space. Write changes to file."""
    if _is_at_limit(items):
        print('You can\'t carry any more items. Drop something first.')
    else:
        items.append(item)
        _save_to_file(STORED_ITEMS_FILE, items)
        print(f'You picked up {item}.')

def get_random_item(items_list: list[str]) -> str:
    """Get a random item from a list fo items."""
    return items_list[randint(0, len(items_list) - 1)].strip()

def give_starter_items() -> list[str]:
    """Give the wizard the selected number of starter items chosen randomly from the all items file."""
    all_wizard_items: list[str] = _get_items_from_file(ALL_ITEMS_FILE)
    return [get_random_item(all_wizard_items) for _ in range(STARTER_ITEM_NUMBER)]

def _save_to_file(target_file: str, items: list[str]) -> None:
    """Private function to save currently stored items into target file."""
    with open(target_file, 'w', encoding='utf-8') as wizard_items_file:
        for item in items:
            wizard_items_file.write(item+'\n')

def _get_items_from_file(file: str) -> list[str]:
    """Private function to read the items from."""
    with open(file, encoding='utf-8') as items_file:
        return items_file.readlines()

def _is_at_limit(items: list[str]) -> bool:
    """Private function to determine if the inventory is at its limit."""
    return True if len(items) >= ITEM_LIMIT else False

def _is_inventory_location(inventory_location: int, items: list[str]) -> bool:
    """Private function to determine if the inventory location is valid."""
    inventory_index: int = inventory_location - 1
    return False if inventory_index < 0 or inventory_index >= len(items) else True

