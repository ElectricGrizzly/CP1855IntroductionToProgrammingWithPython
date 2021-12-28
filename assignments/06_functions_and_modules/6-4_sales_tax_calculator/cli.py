"""CLI entities for displaying information of Sales Tax Calculator program."""

from taxes import get_sales_tax, get_total

def display_title():
    """Display the programs title."""
    print('Sales Tax Calculator')

def display_subtotal(subtotal):
    """Display the subtotal."""
    print(f'Total:\t\t\t{subtotal}')

def display_sales_tax(subtotal):
    """Display the sales tax."""
    print(f'Sales tax:\t\t{get_sales_tax(subtotal)}')

def display_total(subtotal):
    """displays the total with sales tax added."""
    print(f'Total after tax:\t{get_total(subtotal)}')

def display_continue_selection():
    """Return the users selection for program continuation (y/n)."""
    return input('\nAgain? (y/n): ')

def display_farewell():
    """Display a farewell message."""
    print('\nThanks, bye!')