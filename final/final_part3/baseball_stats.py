"""Baseball statistics calculation functions."""

def batting_average(at_bats, hits):
    """Calculates the batting average to 3 decimal places using number of at bats and hits."""
    try:
        return round(hits / at_bats, 3)
    except ZeroDivisionError:
        return round(0, 3)