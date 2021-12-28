"""Calculate and display some statistics based on quarterly sales."""

from sales import list_sum, list_average
from text import display_title, display_total, display_average, display_lowest, display_highest, sales_prompt
from config import QUARTERS

def main() -> None:
    """Display the total, average, lowest, and highest quarter from given quarterly sales values."""
    quarterly_sales: list[float] = []
    display_title()
    for quarter in QUARTERS:
        quarterly_sales.append(float(input(sales_prompt(quarter))))
    quarterly_sales.sort()
    print()
    display_total(list_sum(quarterly_sales))
    display_average(list_average(quarterly_sales))
    display_lowest(quarterly_sales[0])
    display_highest(quarterly_sales[3])

if __name__ == '__main__':
    main()