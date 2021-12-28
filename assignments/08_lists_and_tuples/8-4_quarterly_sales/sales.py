"""Computational functions of the quarterly sales program."""

def list_sum(value_list: list[int|float]) -> None:
    """Return the sum of a list of ints or floats."""
    sum: float = 0
    for value in value_list:
        sum += value
    return sum

def list_average(value_list: list[int|float]) -> None:
    """Return the average of a list of ints or floats."""
    return list_sum(value_list) / len(value_list)