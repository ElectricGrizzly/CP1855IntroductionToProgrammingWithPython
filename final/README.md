# Final Exam
This final practical has three parts. Please read each part carefully and complete each one before moving to the next part. You will have three submissions (you can compress each one and submit one file).
## Part One: Use a list to store the players
Update the program from quiz 2 so that it allows you to store the players for the starting lineup. If you do not have this program please download it. This should include the player’s name, position, at bats, and hits. In addition, the program should calculate the player’s batting average from at bats and hits.
### Console
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
=================================================================
Menu option: 2
Name: Mike
Position: C
At bats: 0
Hits: 0
Mike was added.

Menu option: 1
   Player          POS     AB     H     AVG
-----------------------------------------------------------------
1  Joe             P       10     2     0.2
2  Tom             SS      11     4     0.364
3  Ben             3B      0      0     0.0
4  Mike            C       0      0     0.0

Menu option: 6
Lineup number: 4
You selected Mike AB=0 H=0
At bats: 4
Hits: 1
Mike was updated.

Menu option: 4
Current lineup number: 4
Mike was selected.
New lineup number: 1
Mike was moved.

Menu option: 7
Bye!
```
### Specifications
- Use a list of lists to store each player in the lineup. 
- Use a tuple to store all valid positions (C, 1B, 2B, etc). 
- Make sure that the user’s position entries are valid.
---
## Part Two: Use a file to save the data
Update the program from Part One so it reads the player data from a file when the program starts and writes the player data to a file anytime the data is changed.
### Console
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
=================================================================
Menu option: 1
   Player          POS     AB     H     AVG
-----------------------------------------------------------------
1  Denard          OF      545    174   0.319
2  Joe             2B      475    138   0.291
3  Buster          C       535    176   0.329
4  Hunter          OF      485    174   0.359
5  Brandon         SS      532    125   0.235
6  Eduardo         3B      477    122   0.256
7  Brandon         1B      533    127   0.238
8  Jarrett         OF      215    58    0.27
9  Madison         SP      103    21    0.204

Menu option: 7
Bye!
```
### Specifications
- Use the CSV file to store the lineup.
- Store the functions for writing and reading the file of players in a separate module than the rest of the program.
---
## Part Three: Handle Exceptions
Thoroughly test the program and update it so it handles all exceptions that you encounter
during testing.
### Console
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
### Specifications
- Handle the exception that occurs if the program can’t find the data file. 
- Handle the exceptions that occur if the user enters a string where an integer is expected.
- Handle the exception that occurs if the user enters zero for the number of at bats.