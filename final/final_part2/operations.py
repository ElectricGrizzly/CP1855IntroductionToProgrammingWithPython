"""Operations team manager program."""

from cli import display_lineup_header, display_player, display_player_position, display_player_stats, display_farewell, display_player_updated
from inputs import get_lineup_number, get_string, get_position, get_int
from baseball_stats import batting_average
from files import read_from_file, save_to_file

def display_lineup(players: list[list[str]]) -> None:
    """Displays the lineup of the baseball team."""
    display_lineup_header()
    for index, player in enumerate(players):
        display_player(index + 1, player)

def add_player(players: list[list[str]], players_file: str) -> None:
    """Prompts user for new player information and adds it to team lineup."""
    name: str = get_string('Name: ')
    position: str = get_position('Position: ')
    at_bats: int = get_int('At bats: ')
    hits: int = get_int('Hits: ')
    average: float = batting_average(at_bats, hits)
    players.append([name, position, at_bats, hits, average])
    save_players_to_file(players_file, players)
    print(f'{name} was added.')

def remove_player(players: list[list[str]], players_file: str) -> None:
    """Prompts user for lineup number and remove player from team lineup."""
    lineup_index: int = get_lineup_number('Lineup number: ', players) - 1
    removed_player: list[str] = players.pop(lineup_index)
    save_players_to_file(players_file, players)
    print(f'{removed_player[0]} was removed.')

def move_player(players: list[list[str]], players_file: str) -> None:
    """Prompts user for lineup number and desired new lineup number. Moves player to new lineup position."""
    lineup_index: int = get_lineup_number('Current lineup number: ', players) - 1
    moved_player: list[str] = players.pop(lineup_index)
    print(f'{moved_player[0]} was selected.')
    lineup_index: int = get_lineup_number('New lineup number: ', players) - 1
    players.insert(lineup_index, moved_player)
    save_players_to_file(players_file, players)
    print(f'{moved_player[0]} was moved.')

def edit_player_position(players: list[list[str]], players_file: str) -> None:
    """Prompts user for lineup number and allows user to edit selected players position."""
    lineup_index: int = get_lineup_number('Lineup number: ', players) - 1
    selected_player: list[str] = players[lineup_index]
    display_player_position(selected_player)
    selected_player[1] = get_position('New position: ')
    save_players_to_file(players_file, players)
    display_player_updated(selected_player)

def edit_player_stats(players: list[list[str]], players_file: str) -> None:
    """Prompts user for lineup number and allows user to edit selected players statistics."""
    lineup_index: int = get_lineup_number('Lineup number: ', players) - 1
    selected_player: list[str] = players[lineup_index]
    display_player_stats(selected_player)
    selected_player[2] = get_int('At bats: ')
    selected_player[3] = get_int('Hits: ')
    selected_player[4] = batting_average(selected_player[2], selected_player[3])
    save_players_to_file(players_file, players)
    display_player_updated(selected_player)

def finish(players: list[list[str]], players_file: str) -> None:
    """Close the program."""
    save_players_to_file(players_file, players)
    display_farewell()
    quit()

def read_players_from_file(file: str) -> None:
    players = read_from_file(file)
    for player in players:
        player[2] = int(player[2])
        player[3] = int(player[3])
        player[4] = float(player[4])
    return players

def save_players_to_file(file: str, players: list[list[str]]) -> None:
    save_to_file(file, players)

def run_option(option: int, players: list[list[str]], players_file: str) -> None:
    """Run the function specified by option."""
    if option == 1:
        display_lineup(players)
    elif option == 2:
        add_player(players, players_file)
    elif option == 3:
        remove_player(players, players_file)
    elif option == 4:
        move_player(players, players_file)
    elif option == 5:
        edit_player_position(players, players_file)
    elif option == 6:
        edit_player_stats(players, players_file)
    else:
        finish(players, players_file)