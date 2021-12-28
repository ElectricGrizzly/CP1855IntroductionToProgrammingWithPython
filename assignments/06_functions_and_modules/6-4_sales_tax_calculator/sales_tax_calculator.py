from cli import display_title, display_subtotal, display_sales_tax, display_total, display_continue_selection, display_farewell

def item_cost_entry() -> float:
    """Return the sum of all user entries."""
    print('\nENTER ITEMS (ENTER 0 TO END)')
    subtotal: float = 0.0
    while True:
        cost: float = float(input('Cost of item: '))
        if cost == 0:
            break
        else:
            subtotal += cost
    return subtotal

def main():
    """Calculate and display the subtotal, sales tax and total of a number of users input costs."""
    display_title()
    while True:
        subtotal: float = item_cost_entry()
        display_subtotal(subtotal)
        display_sales_tax(subtotal)
        display_total(subtotal)
        continue_selection = display_continue_selection()
        if continue_selection != 'y':
            display_farewell()
            break
    
if __name__ == '__main__':
    main()