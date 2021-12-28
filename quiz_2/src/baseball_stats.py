"""This file provides functions for calculating baseball statistics"""

def batting_average(at_bats, hits):
    """Calculates the batting average to 3 decimal places using number of at bats and hits"""
    return round(hits / at_bats, 3)