"""Calculations used by Sales Tax Calculator program."""

# The sales tax rate as a %, must divide by 100 for a decimal value.
SALES_TAX_RATE = 6

def get_sales_tax(subtotal):
    """Return the sales tax of a given value."""
    return round(subtotal * SALES_TAX_RATE/100, 2)

def get_total(subtotal):
    """Return the total of given subtotal with tax added."""
    return round(subtotal * (1 + SALES_TAX_RATE/100), 2)