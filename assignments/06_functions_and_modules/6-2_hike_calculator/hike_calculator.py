"""Takes a number of miles and converts it to a feet value."""

def main() -> None:
    """Convert the user input miles value to feet and display the result."""
    print('Hike Calculator')
    miles: float = float(input('How many miles did you walk?: '))
    print(f'You walked {to_feet(miles)} feet.')

def to_feet(miles: float) -> int:
    """Return the input miles value as feet."""
    FEET_PER_MILE: int = 5280
    return int(miles * FEET_PER_MILE)

if __name__ == '__main__':
    main()