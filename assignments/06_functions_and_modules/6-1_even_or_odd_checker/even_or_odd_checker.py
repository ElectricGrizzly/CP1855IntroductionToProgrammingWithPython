"""Check if an integer is even or odd."""

def main() -> None:
    """Determine if the user input integer is even or odd and display the result."""
    print('Even or Odd Checker')
    integer: int = int(input('Enter an integer: '))
    print(f'This is an {is_even(integer)} number.')

def is_even(value: int) -> str:
    """Return 'even' or 'odd' depending on if the value is divisible by 2."""
    if value % 2 == 0 or value == 0:
        return 'even'
    else:
        return 'odd'

if __name__ == '__main__':
    main()