"""Handling game rules stored as text ."""

def is_rule(line: str, starting_chr: str = '*', omit: str = 'NOTE') -> bool:
    """If the first character of the line is the selected character and the line doesn't contain the omitted text (case-sensitive)."""
    return True if line.startswith(starting_chr) and line.find(omit) == -1 else False

def display_rules(rules: list[str], starting_chr: str = '*', omit: str = 'NOTE') -> None:
    """Print the rules matching the specifications to console. Removes leading/trailing whitespace and newlines."""
    for line in rules:
        if is_rule(line, starting_chr, omit):
            print(line.strip())