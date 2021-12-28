"""Module of functions that perform baseball statistics calculations."""

def batting_average(at_bats, hits):
    """Calculates the batting average to 3 decimal places using number of at bats and hits."""
    return round(hits / at_bats, 3) if at_bats else 0.0