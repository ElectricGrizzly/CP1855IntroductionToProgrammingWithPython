"""Tip calculator program."""
from controls import display_title, get_meal_information, display_results

def main():
    """Provide meal information based on meal cost and tip percentage."""
    display_title()
    meal_cost, tip_percentage, tip_cost, total_cost = get_meal_information()
    display_results(meal_cost, tip_percentage, tip_cost, total_cost)

if __name__ == '__main__':
    main()