"""Converts the input feet to meters or vice-versa based on user selection."""

from conversions import to_feet, to_meters

def main():
    """Perform the user selected distance conversion and display the result."""
    continue_selection: str = 'y'
    display_title()
    while continue_selection.lower() == 'y':
        display_menu()
        conversion_selection: str = input('Select a conversion (a/b): ')
        if conversion_selection == 'a':
            feet: float = float(input('\nEnter feet: '))
            print(f'{round(to_meters(feet), 2)} meters\n')
        else:
            meters: float = float(input('\nEnter meters: '))
            print(f'{round(to_feet(meters), 2)} feet\n')
        print()
        continue_selection = input('Woulds you like to perform another conversion? (y/n): ')
    display_farewell()

def display_title():
    """Display the programs title."""
    print('Feet and Meters Converter\n')

def display_menu():
    """Display the program option menu."""
    print('Conversions Menu:\n' +
        'a. Feet to Meters\n' +
        'b. Meters to Feet'
        )

def display_farewell():
    """Display farewell message."""
    print('\nThanks, bye!')

if __name__ == '__main__':
    main()