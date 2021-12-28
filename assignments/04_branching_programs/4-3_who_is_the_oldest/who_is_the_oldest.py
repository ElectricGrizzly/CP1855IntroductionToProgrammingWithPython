"""Determine the oldest age from three provided ages."""

def main() -> None:
    """Take three input ages and provide the oldest age."""
    age_one: int = int(input('Enter 1st age: '))
    age_two: int = int(input('Enter 2nd age: '))
    age_three: int = int(input('Enter 3rd age: '))

    ages: list[int] = [age_one, age_two, age_three]
    ages.sort()
    oldest: int = ages[-1]

    print(f'Oldest is {oldest}')

if __name__ == "__main__":
    main()
