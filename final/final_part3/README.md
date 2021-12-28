# Part Three: Handle Exceptions
Thoroughly test the program and update it so it handles all exceptions that you encounter
during testing.
## Console
```
=================================================================
                       Baseball Team Manager
MENU OPTIONS
1 - Display lineup
2 - Add player
3 - Remove player
4 - Move player
5 - Edit player position
6 - Edit player stats
7 - Exit program

POSITIONS
C, 1B, 2B, 3B, SS, LF, CF, RF, P

Team data file could not be found.
You can create a new one if you want.
=================================================================
Menu option: 2
Name: Mike
Position: SS
At bats: 0
Hits: 0
Mike was added.

Menu option: X
Not a valid option. Please try again.

MENU OPTIONS
1 - Display lineup
2 - Add player
3 - Remove player
4 - Move player
5 - Edit player position
6 - Edit player stats
7 - Exit program

Menu option: 7
Bye!
```
## Specifications
- Handle the exception that occurs if the program can’t find the data file. 
- Handle the exceptions that occur if the user enters a string where an integer is expected.
- Handle the exception that occurs if the user enters zero for the number of at bats.