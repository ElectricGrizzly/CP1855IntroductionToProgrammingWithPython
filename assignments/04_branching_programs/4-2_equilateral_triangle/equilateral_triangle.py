"""Determines if a triangle is equilater based on three input side lengths."""

def main() -> None:
    """Takes user input of three side lengths and displays if triangle is equilateral or not."""
    length_one: int = int(input('Enter the first side: '))
    length_two: int = int(input('Enter the second side: '))
    length_three: int = int(input('Enter the third side: '))
    lengths: set[int] = {length_one, length_two, length_three}
    
    print('The triangle is not equilateral') if len(lengths) != 1 else print('The triangle is equilateral')

if __name__ == "__main__":
    main()