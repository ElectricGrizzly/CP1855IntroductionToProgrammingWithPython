"""Conversions and constants for Feet and Metere Converter program."""

METERS_PER_FOOT = 0.3048

def to_feet(meters: float) -> float:
    """Return the meter value as feet."""
    return meters / METERS_PER_FOOT

def to_meters(feet: float) -> float:
    """Return the feet value as meters"""
    return feet * METERS_PER_FOOT