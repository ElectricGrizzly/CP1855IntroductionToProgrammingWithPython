"""Determine the shipping cost and total cost of an item order."""

from config import SHIPPING_MINIMUMS, DIVIDER

def display_header():
    """Display the program title."""
    print(DIVIDER)
    print("Shipping Calculator")
    print(DIVIDER)

def display_shipping_table():
    """Display the shipping table."""
    print(DIVIDER)
    print("COST OF ITEMS SHIPPING COST")
    print(DIVIDER)
    print("< 30.00 5.95")
    print("30.00-49.99 7.95")
    print("50.00-74.99 9.95")
    print("> 75.00 FREE")
    print(DIVIDER)

def get_order_total() -> float:
    """Returns the order total after ensuring the input value is > 0."""
    while True:
        order_total: float = float(input('Cost of items ordered: '))
        if order_total >= 0:
            return order_total
        else:
            print('You must enter a positive number. Please try again.')

def get_shipping_cost(cost: float) -> float:
    """Returns the order total as determined by the items cost."""
    for shipping_cost in SHIPPING_MINIMUMS:
            if cost >= SHIPPING_MINIMUMS[shipping_cost]:
                return shipping_cost


def main() -> None:
    """Take user input for the item cost and display claculated shipping cost and total cost."""
    display_header()
    display_shipping_table()
    continue_character: str = 'y'
    while continue_character == 'y':
        order_cost: float = get_order_total()
        shipping_cost: float = get_shipping_cost(order_cost)
        print(f'Shipping cost: {shipping_cost if shipping_cost != 0 else "FREE"}')
        print(f'Total cost: {round(order_cost + shipping_cost, 2)}')
        continue_character: str = input('Continue? (y/n): ')
        print(DIVIDER)
    print('Bye!')

if __name__ == "__main__":
    main()
    