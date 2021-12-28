"""Calculate the per unit price of two similar items."""

def main() -> None:
    """Take user price input and provide per unit cost to user."""
    MASS_UNIT: str = 'oz'
    MASS_ONE: int = 64
    MASS_TWO: int = 32
    print('Price Comparison\n')

    price_one: float = float(input(f'Price of {MASS_ONE} {MASS_UNIT} size: '))
    price_two: float = float(input(f'Price of {MASS_TWO} {MASS_UNIT} size: '))

    per_unit_one: float = round(price_one / MASS_ONE, 2)
    per_unit_two: float = round(price_two / MASS_TWO, 2)

    print(f'Price per {MASS_UNIT} ({MASS_ONE} {MASS_UNIT}): {per_unit_one}')
    print(f'Price per {MASS_UNIT} ({MASS_TWO} {MASS_UNIT}): {per_unit_two}')

if __name__ == '__main__':
    main()


    
