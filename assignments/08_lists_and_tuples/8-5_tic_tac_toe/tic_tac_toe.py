"""Tic Tac Toe game."""

from game import make_move, is_win, change_player
from text import display_grid, display_player_turn, display_winner, display_farewell, display_tie
from config import GRID, PLAYERS, VERTICE, VERTICAL_BORDER, HORIZONTAL_BORDER, MOVES

def main():
    """Perform a players' move if able and check for a win."""
    players: list[str] = PLAYERS
    player: str = players[0]
    moves: int = 0

    game_grid: list[list[str]] = GRID
    display_grid(game_grid, VERTICE, VERTICAL_BORDER, HORIZONTAL_BORDER)

    while True:
        display_player_turn(player)

        make_move(player, game_grid)
        moves += 1
        
        display_grid(game_grid, VERTICE, VERTICAL_BORDER, HORIZONTAL_BORDER)

        if is_win(game_grid):
            display_winner(player)
            break

        if moves == MOVES:
            display_tie()
            break

        player = change_player(player, players)
    display_farewell()

if __name__ == '__main__':
    main()
        