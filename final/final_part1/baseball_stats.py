"""Baseball statistics calculation functions."""

def batting_average(at_bats, hits) -> float:
    """Calculates the batting average to 3 decimal places using number of at bats and hits."""
    return round(hits / at_bats, 3) if at_bats else 0.0