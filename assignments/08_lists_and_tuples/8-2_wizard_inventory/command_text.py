"""Text and print for the commands of the wizard inventory program."""

NUMBER_PROMPT = 'Number: '
NAME_PROMPT = 'Name: '
ITEM_UPDATE_PROMPT = 'Updated name: '

def display_add_error() -> None:
    """Display error when attempting to add more items than the item limit allows."""
    print('You can\'t carry any more items. Drop something first.')

def display_item_info(item_number: int, item: str) -> None:
    """Display the item number and item name."""
    print(f'{item_number}. {item}')

def display_item_added(item: str) -> None:
    """Display which item was added."""
    print(f'{item} was added.')

def display_drop_error(item_number: int) -> None:
    """Display error when trying to drop an item number that doesnt exist."""
    print(f'You don\'t have an item number {item_number} to drop.')

def display_edit_error(item_number: int) -> None:
    """Display error when trying to edit an item number that doesnt exist."""
    print(f'You don\'t have an item number {item_number} to edit.')

def display_item_dropped(item: str) -> None:
    """Display which item was droped."""
    print(f'{item} was dropped.')

def display_item_edited(item_number: int) -> None:
    """Display the item number of the edited item."""
    print(f'Item number {item_number} was updated')