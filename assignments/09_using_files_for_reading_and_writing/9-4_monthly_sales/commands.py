"""Monthly sales program command functions."""

from csv import reader, writer
from config import MONTHLY_SALES_FILE

def read_sales_file() -> None:
    """Read the monthly sales file from configuration."""
    with open(MONTHLY_SALES_FILE, encoding='utf-8') as monthly_sales_file:
        csv = reader(monthly_sales_file)
        return [row for row in csv]

def view_monthly_sales(sales: list[list[str]]) -> None:
    """Display monthly sales to console."""
    for row in sales:
        print(f'{row[0]} - {row[-1]}')

def view_yearly_summary(sales: list[list[str]]) -> None:
    """Calculate and display yearly sales summary."""
    yearly_total: int = calculate_yearly_total(sales)
    print(f'Yearly total: {yearly_total}')
    monthly_average: float = calculate_monthly_average(sales)
    print(f'Monthly average: {round(monthly_average, 2)}')

def calculate_yearly_total(sales: list[list[str]]) -> int:
    """Calculate the total yearly sales."""
    total: int = 0
    for row in sales:
        total += int(row[-1])
    return total

def calculate_monthly_average(sales: list[list[str]]) -> float:
    """Calculate the monthly sale average."""
    return calculate_yearly_total(sales) / len(sales)

def edit_month(sales: list[list[str]]) -> None:
    """Edit the month designated by the three letter month abbreviation."""
    month_abbreviation: str = input('Three-letter Month: ')
    for row in sales:
        if row[0] == month_abbreviation.capitalize():
            new_amount: int = int(input('Sales Amount: '))
            row[-1] = str(new_amount)
            _save_to_csv(sales)
            print(f'Sales amount for {row[0]} was modified.')
            return
    print(f'{month_abbreviation} is not a valid abbreviation!')

def _save_to_csv(sales: list[list[str]]) -> None:
    """Save sales data to target file from configuration."""
    with open(MONTHLY_SALES_FILE, 'w', newline='', encoding='utf-8') as monthly_sales_file:
        csv = writer(monthly_sales_file)
        csv.writerows(sales)