"""CLI and text entities of tic tac toe game."""

def display_grid(grid: list[list[str]], vertice_chr, vert_chr, hori_chr) -> None:
    """Display the current tic tac toe grid."""
    print()
    for row in grid:
        _display_horizontal_divider(grid, vertice_chr, hori_chr)
        _display_row(row, vert_chr)
    _display_horizontal_divider(grid, vertice_chr, hori_chr)
    print()

def _display_horizontal_divider(grid: list[list[str]], vertice_chr, border_chr) -> None:
    """Display the horizontal divider for the grid."""
    print(((vertice_chr+border_chr)*len(grid))+vertice_chr)

def _display_row(row: list[str], border_chr) -> None:
    """Display the row with dividers between values for the grid."""
    display: str = ''
    for value in row:
        display += f'{border_chr} {value} '
    print(display + border_chr)

def display_farewell() -> None:
    """Display a farewell message."""
    print('Game over!')

def display_player_turn(player: str) -> None:
    """Display the current players turn."""
    print(f'{player}\'s turn')

def display_winner(player: str) -> None:
    """Display the winner of the game."""
    print(f'{player} wins!\n')

def display_tie() -> None:
    """Display indication that the game is a tie."""
    print('It\'s a tie!\n')

