"""Generate a table of squares and cubes from the provided integer range."""

def get_endpoints() -> tuple[int]:
    """Get the start and stop values for the tables range."""
    while True:
        start: int = int(input('Start number:\t'))
        stop: int = int(input('Stop number:\t'))
        if start > stop:
            print("You must enter a start value <= stop value!")
        else:
            return start, stop

def display_table_header() -> None:
    """Display a tab-aligned header for the table."""
    print()
    print('Number\t','Squared\t', 'Cubed')
    print('='*len('Number'),'\t', '='*len("Squared"),'\t', '='*len('Cubed'))

def display_table_data(start: int, stop: int) -> None:
    """Display the calculated table data by row."""
    for number in range(start, stop + 1):
        print(number, '\t', number**2, '\t\t', number**3)

def main() -> None:
    """Take a users start and stop values and display a table of squares and cubes of that range."""
    print('Table of Powers\n')
    start, stop = get_endpoints()
    display_table_header()
    display_table_data(start, stop)

if __name__ == '__main__':
    main()