# Part One: Use a list to store the players
Update the program from quiz 2 so that it allows you to store the players for the starting lineup. If you do not have this program please download it. This should include the player’s name, position, at bats, and hits. In addition, the program should calculate the player’s batting average from at bats and hits.
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
## Specifications
- Use a list of lists to store each player in the lineup. 
- Use a tuple to store all valid positions (C, 1B, 2B, etc). 
- Make sure that the user’s position entries are valid.