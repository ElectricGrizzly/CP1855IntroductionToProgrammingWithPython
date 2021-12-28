"""Monthly sales program command functions."""

from sys import exit
from csv import reader, writer

def read_sales_file(file: str) -> None:
    """Read the monthly sales file from configuration."""
    try:
        with open(file, encoding='utf-8') as monthly_sales_file:
            csv = reader(monthly_sales_file)
            return [row for row in csv]
    except FileNotFoundError:
        print('Monthly Sales file not found!')
        print('Exiting program. Bye!')
        exit()

def view_monthly_sales(sales: list[list[str]]) -> None:
    """Display monthly sales to console."""
    for row in sales:
        print(f'{row[0]} - {row[-1]}')

def view_yearly_summary(sales: list[list[str]]) -> None:
    """Calculate and display yearly sales summary."""
    yearly_total: int = calculate_yearly_total(sales)
    print(f'Yearly total: {yearly_total}')
    monthly_average: float = calculate_monthly_average(yearly_total, sales)
    print(f'Monthly average: {round(monthly_average, 2)}')

def calculate_yearly_total(sales: list[list[str]]) -> int:
    """Calculate the total yearly sales."""
    total: int = 0
    for row in sales:
        total += _convert_monthly_sales_to_int(row)
    return total

def _convert_monthly_sales_to_int(row: list[str]) -> int:
    """Convert sales value of row to int or 0 if invalid format."""
    try:
        return int(row[-1])
    except ValueError:
        print(f'Using sales amount of 0 for {row[0]}.')
        return 0

def calculate_monthly_average(total: int, sales: list[list[str]]) -> float:
    """Calculate the monthly sale average."""
    return total / len(sales)

def edit_month(sales: list[list[str]], file: str) -> None:
    """Edit the month designated by the three letter month abbreviation."""
    try:
        month_abbreviation: str = input('Three-letter Month: ')
        for row in sales:
            if row[0] == month_abbreviation.capitalize():
                new_amount: str = input('Sales Amount: ')
                row[-1] = new_amount
                _save_to_csv(file, sales)
                print(f'Sales amount for {row[0]} was modified.')
                return
        raise NameError('Not a valid month abbreviation')
    except NameError as exception:
        print(exception)
        return edit_month(sales)

def _save_to_csv(file: str, sales: list[list[str]]) -> None:
    """Save sales data to target file from configuration."""
    with open(file, 'w', newline='', encoding='utf-8') as monthly_sales_file:
        csv = writer(monthly_sales_file)
        csv.writerows(sales)