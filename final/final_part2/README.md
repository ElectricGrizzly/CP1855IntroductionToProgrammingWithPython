# Part Two: Use a file to save the data
Update the program from Part One so it reads the player data from a file when the program starts and writes the player data to a file anytime the data is changed.
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
## Specifications
- Use the CSV file to store the lineup.
- Store the functions for writing and reading the file of players in a separate module than the rest of the program.