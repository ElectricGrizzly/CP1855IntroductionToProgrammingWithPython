"""Calculate the tip amount and total meal cost from three specific tip percentages and the meal sub total before the tip."""

from config import TIPS

def main() -> None:
    """Calculate tip amounts and total cost from input meal cost for each tip percentage."""
    print('Tip Calculator\n')

    meal_cost: float = float(input('Cost of meal:\t'))

    for tip in TIPS:
        print()
        print(f'{tip}%')
        tip_amount: float = round(meal_cost * tip / 100, 2)
        total_amount: float = round(meal_cost + tip_amount, 2)
        print(f'Tip amount:\t{tip_amount}')
        print(f'Total amount:\t{total_amount}')
  
if __name__ == "__main__":
    main()