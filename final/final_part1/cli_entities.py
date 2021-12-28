"""Module of constant entities for use by CLI."""

from config import valid_positions

HORIZONTAL_DIVIDER = '='
CONSOLE_LENGTH = 72
PROGRAM_TITLE = 'Baseball Team Manager'
MENU_TITLE = 'MENU OPTIONS'
MENU_OPTIONS = (
    'Display lineup',
    'Add player',
    'Remove player',
    'Move player',
    'Edit player position',
    'Edit player stats',
    'Exit program'
)
POSITION_TITLE = 'POSITIONS'
POSITIONS = valid_positions
LINEUP_NUMBER_TITLE = '#'
LINEUP_NUMBER_LENGTH = 6
LINEUP_PLAYER_TITLE = 'Player'
LINEUP_PLAYER_LENGTH = 38
LINEUP_POSITION_TITLE = 'POS'
LINEUP_POSITION_LENGTH = 8
LINEUP_AT_BATS_TITLE = 'AB'
LINEUP_AT_BATS_LENGTH = 6
LINEUP_HITS_TITLE = 'H'
LINEUP_HITS_LENGTH = 6
LINEUP_AVERAGE_TITLE = 'AVG'
LINEUP_AVERAGE_LENGTH = 8
LINEUP_DIVIDER = '-'
INVALID_OPTION = 'Not a valid option. Please try again.'
FAREWELL = 'Bye!'
