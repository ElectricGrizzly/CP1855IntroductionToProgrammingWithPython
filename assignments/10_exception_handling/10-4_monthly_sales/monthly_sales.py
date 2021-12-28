"""Monthly sales program."""

from config import MONTHLY_SALES_FILE
from commands import read_sales_file, view_monthly_sales, view_yearly_summary, edit_month
from text import display_title, display_menu, display_invalid_command, display_farewell, COMMAND_PROMPT

def main():
    """Main function for monthly sales program."""
    display_title()
    monthly_sales: list[list[str]] = read_sales_file(MONTHLY_SALES_FILE)
    display_menu()
    while True:
        command: str = input(COMMAND_PROMPT)
        if command == 'monthly':
            view_monthly_sales(monthly_sales)
        elif command == 'yearly':
            view_yearly_summary(monthly_sales)
        elif command == 'edit':
            edit_month(monthly_sales, MONTHLY_SALES_FILE)
        else:
            if command == 'exit':
                break
            display_invalid_command(command)
        print()
    display_farewell()

if __name__ == '__main__':
    main()