"""Rolls a six sides die and displays information on the roll."""

from random import randint

def main():
    """Rolls two dice and presents the results to user."""
    display_title()
    roll_selection = get_roll_selection('\nRoll the dice? (y/n): ')
    while roll_selection == 'y':
        die1 = roll_die1()
        die2 = roll_die2()
        get_total(die1, die2)
        if is_boxcar(die1, die2):
            print('Boxcars!')
        elif is_snake_eyes(die1, die2):
            print('Snake eyes!')
        roll_selection = get_roll_selection()

def roll_die():
    """Return a random integer from 1-6."""
    return randint(1, 6)

def get_sum(value1, value2):
    """Return the sum of two values."""
    return value1 + value2

def display_title():
    """Print the programs title."""
    print("Dice Roller")

def get_roll_selection(prompt:str = '\nRoll again? (y/n): '):
    """Return the users character when prompted to continue (y/n)."""
    return input(prompt)

def is_boxcar(die1, die2):
    """Return true if face values of die total 12."""
    BOXCARS = 12
    return True if (die1 + die2 == BOXCARS) else False

def is_snake_eyes(die1, die2):
    """Return true if face values of die total 2."""
    SNAKE_EYES = 2
    return True if (die1 + die2 == SNAKE_EYES) else False

def roll_die1():
    """Return the first die value after printing value to display."""
    die_value = roll_die()
    print(f'\nDie 1: {die_value}')
    return die_value

def roll_die2():
    """Return the second die value after printing value to display."""
    die_value = roll_die()
    print(f'Die 2: {die_value}')
    return die_value

def get_total(die1, die2):
    """Return the total of the die values after printing total value to display."""
    total = get_sum(die1, die2)
    print(f'Total: {total}')
    return total

if __name__ == '__main__':
    main()