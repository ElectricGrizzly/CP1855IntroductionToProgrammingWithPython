"""Pig Dice Rules program."""

from rules import display_rules

def main() -> None:
    """Display the Pig Dice rules with some minor filtering."""
    with open('rules.txt', encoding='utf-8') as rules:
        text_content: list[str] = rules.readlines()
        print('Pig Dice Rules:')
        display_rules(text_content)

if __name__ == '__main__':
    main()