"""Provide a student with their password based on their name and birth year."""

def main() -> None:
    """Takes student input and provides a template based temporary password."""
    print('Registration Form\n')

    first_name: str = input('First name:\t')
    last_name: str = input('Last name:\t')
    full_name: str = first_name + ' ' + last_name
    birth_year: str = input('Birth year:\t')
    password: str = first_name + '*' + birth_year

    print(f'\nWelcome {full_name}!')
    print('Your registration is complete.')
    print(f'Your temporary password is: {password}')

if __name__ == '__main__':
    main()