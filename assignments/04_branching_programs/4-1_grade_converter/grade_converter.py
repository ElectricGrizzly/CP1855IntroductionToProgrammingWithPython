"""Determines corresponding letter grade from input numerical grade."""

from config import GRADE_MINIMUMS

def main() -> None:
    """Take user numerical grade input and provide letter grade equivalent. Continue until user enters 'n'"""
    print('Letter Grade Converter')
    continue_character: str = 'y'
    while(continue_character.lower() == 'y'):
        print()
        numerical_grade: int = int(input('Enter numerical grade: '))
        for grade in GRADE_MINIMUMS:
            if numerical_grade >= GRADE_MINIMUMS[grade]:
                print(f'Letter grade: {grade}\n')
                break
        continue_character: str = input('Continue? (y/n): ')
    print('Bye!')

if __name__ == "__main__":
    main()
