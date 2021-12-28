"""Commands of the wizard inventory program."""

from config import ITEM_LIMIT

def show_items(items: list[str]) -> None:
    """Show the items in the inventory."""
    for index, item in enumerate(items):
        print(f'{index + 1}. {item}')

def grab_item(items: list[str]) -> None:
    """Grab an item and add it to inventory if there is space."""
    if len(items) >= ITEM_LIMIT:
        print('You can\'t carry any more items. Drop something first.')
    else:
        items.append(input('Name: '))
        print(f'{items[-1]} was added')

def edit_item(items: list[str]) -> None:
    """Edit an item at a specified inventory location."""
    item_index = int(input('Number: ')) - 1
    if item_index < 0 or item_index >= len(items):
        print(f'There is no item number {item_index + 1}!')
    else:
        print()
        items[item_index] = input('Updated name: ')
        print(f'Item number {item_index + 1} was updated')

def drop_item(items: list[str]) -> None:
    """Drop an item at the specified inventory location."""
    item_index = int(input('Number: ')) - 1
    if item_index < 0 or item_index >= len(items):
        print(f'There is no item number {item_index + 1}!')
    else:
        item = items.pop(item_index)
        print(f'{item} was dropped')
