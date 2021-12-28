"""Text and CLI entities for user interaction."""

def display_title():
    """Display the program title."""
    print('The Quarterly Sales Program\n')

def display_total(total: int|float):
    """Display the calculated total."""
    print(f'Total: {round(total, 2)}')

def display_average(average: int|float):
    """Display the calculated average."""
    print(f'Average Quarter: {round(average, 2)}')

def display_lowest(lowest: int|float):
    """Display the lowest quarter."""
    print(f'Lowest Quarter: {round(lowest, 2)}')

def display_highest(highest: int|float):
    """Display the highest quarter."""
    print(f'Highest Quarter: {round(highest, 2)}')

def sales_prompt(quarter: int):
    """Prompt for the total sales of a quarter."""
    return f'Enter sales for Q{quarter}: '