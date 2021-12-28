"""Calculate the estimated travel time from distance and speed to the nearest minute."""

def main() -> None:
    """Take user input speed and distance and provide travel time to the nearest minute."""
    print('Travel Time Calculator\n')

    distance: int = int(input('Enter miles: '))
    speed: int = int(input('Enter miles per hour: '))

    hours: int = distance // speed
    minutes: int = round((distance / speed - hours) * 60)

    print('\nEstimated travel time')
    print(f'Hours: {hours}')
    print(f'Minutes: {minutes}')
    
if __name__ == "__main__":
    main()
    
