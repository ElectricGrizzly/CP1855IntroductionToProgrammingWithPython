"""Functions for Tic Tac Toe game."""

def is_all_equal(value_list: list[str]) -> bool:
    """Check if all values in a list are equal."""
    start: str = value_list[0]
    return True if value_list.count(start) == len(value_list) and start != ' ' else False

def row_win(grid: list[list[str]]) -> bool:
    """Check if any wins exist in the grid rows."""
    for row in grid:
        if is_all_equal(row):
            return True
    return False

def column_win(grid: list[list[str]]) -> bool:
    """Check if any wins exist in the grid columns."""
    for value in range(len(grid)):
        column = [row[value] for row in grid]
        if is_all_equal(column):
            return True
    return False

def diagonal_win(grid: list[list[str]]) -> bool:
    """Check if any wins exist in the diagonals of the grid."""
    front_diagonal: list[str] = [row[index] for index, row in enumerate(grid)]
    if is_all_equal(front_diagonal):
        return True
    back_diagonal: list[str] = [row[-index - 1] for index, row in enumerate(grid)]
    if is_all_equal(back_diagonal):
        return True
    return False

def is_win(grid: list[list[str]]) -> None:
    """Check if a win is present."""
    if row_win(grid):
        return True
    if column_win(grid):
        return True
    if diagonal_win(grid):
        return True
    return False

def make_move(player: str, grid: list[list[str]]) -> None:
    """Make a move at the indicated grid position."""
    row: int = get_row(grid)
    column: int = get_column(grid)
    if grid[row-1][column-1] != ' ':
        print(f'A player has already made a move at [row: {row}, column: {column}]!')
        return make_move(player, grid)
    else:
        grid[row-1][column-1] = player

def change_player(current_player: str, players: list[str]) -> None:
    """Change the player fron the current player to the other player."""
    return players[0] if current_player != players[0] else players[1]

def get_row(grid: list[list[str]]) -> None:
    """Get the desired row for a move."""
    row: int = int(input(f'Pick a row ({", ".join([str(value+1) for value in range(len(grid))])}): '))
    if row > len(grid) or row < 1:
        print(f'"{row}" is not a valid row!')
        return get_row(grid)
    else:
        return row

def get_column(grid: list[list[str]]) -> None:
    """Get the desired column for a move."""
    column: int = int(input(f'Pick a column ({", ".join([str(value+1) for value in range(len(grid))])}): '))
    if column > len(grid) or column < 1:
        print(f'"{column}" is not a valid column!')
        return get_column(grid)
    else:
        return column