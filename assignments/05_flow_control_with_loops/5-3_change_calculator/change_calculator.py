"""Calculates the quantities of coins to represent a number of cents."""

def make_change(cents: int) -> tuple[int]:
    """Returns the number of quarters, dimes, nickels, and pennies from a given number of cents."""
    QUARTER_VALUE: int = 25
    DIME_VALUE: int = 10
    NICKEL_VALUE: int = 5

    pennies: int = cents

    quarters: int = pennies // QUARTER_VALUE
    pennies -= quarters * QUARTER_VALUE

    dimes: int = pennies // DIME_VALUE
    pennies -= dimes * DIME_VALUE

    nickels: int = pennies // NICKEL_VALUE
    pennies -= nickels * NICKEL_VALUE

    return quarters, dimes, nickels, pennies

def display_change(quarters: int, dimes: int, nickels: int, pennies: int) -> None:
    """Displays the coin quantities for change in tabulated form."""
    print("Quarters:\t", quarters)
    print("Dimes:\t\t", dimes)
    print("Nickels:\t", nickels)
    print("Pennies:\t", pennies)

def main() -> None:
    """Calculated the quantities of coins for an inputed number of cents."""
    print('Change Calculator')
    continue_character: str = 'y'
    while continue_character.lower() == 'y':
        print()
        cents: int = int(input('Enter number of cents (0-99): '))
        quarters, dimes, nickels, pennies = make_change(cents)
        print()
        display_change(quarters, dimes, nickels, pennies)
        continue_character: str = input('\nContinue? (y/n): ')
    print('Bye!')

if __name__ == "__main__":
   main()
