"""Control functions of tip calculator program."""

def display_results(meal_cost: float, tip_percentage: int, tip_cost: float, total_cost: float) -> None:
    """Print the meal results in tabulated form."""
    print('\nOUTPUT')
    print(f'Cost of meal: {round(meal_cost, 2)}')
    print(f'Tip percent: {round(tip_percentage, 2)}%')
    print(f'Tip amount: {round(tip_cost, 2)}')
    print(f'Total Amount: {round(total_cost, 2)}')

def display_title() -> None:
    """Print the title of the program."""
    print('Tip Calculator\n')

def get_meal_information() -> None:
    """Calculate meal information and return the values in a tuple."""
    try:
        print('INPUT')
        meal_cost: float = get_meal_cost()
        tip_percentage: int = get_tip_percentage()
        tip_cost: float = get_tip_cost(meal_cost, tip_percentage)
        total_cost: float = get_total_cost(meal_cost, tip_cost)
        return meal_cost, tip_percentage, tip_cost, total_cost
    except Exception as exception:
        print('Whatever you did, please don\'t do that again.\n', exception)
        return get_meal_information()

def get_total_cost(meal_cost: float, tip_cost: float) -> float:
    """Calculate the total meal cost from the tip cost and meal cost."""
    return meal_cost + tip_cost

def get_tip_cost(meal_cost: float, tip_percentage: int) -> float:
    """Calculate the tip cost from the meal cost and tip percentage."""
    PERCENT = 100
    return meal_cost * tip_percentage / PERCENT

def get_meal_cost():
    """Get the meal cost from the user, check that the cost is > 0."""
    try:
        meal_cost: float = _get_meal_cost()
        if meal_cost <= 0:
            raise ValueError('Must be greater than 0. Please try again')
        return meal_cost
    except ValueError as exception:
        print(exception)
        return get_meal_cost()

def _get_meal_cost():
    """Private function to get meal cost from user, check that the cost is valid float."""
    try:
        return float(input('Cost of meal: '))
    except ValueError:  # Using built-in ValueError raised by float conversion
        print('Must be a valid decimal number. Please try again.')
        return _get_meal_cost()

def get_tip_percentage():
    """Get the tip percentage from user, check that the percentage is > 0."""
    try:
        tip_percentage: int = _get_tip_percentage()
        if tip_percentage <= 0:
            raise ValueError('Must be greater than 0. Please try again')
        return tip_percentage
    except ValueError as exception:
        print(exception)
        return get_tip_percentage()

def _get_tip_percentage():
    """Private function to get tip percentage from user, check that the cost is valid int."""
    try:
        return int(input('Tip percent: '))
    except ValueError as exception:
        print('Must be a valid integer. Please try again.')
        return _get_tip_percentage()