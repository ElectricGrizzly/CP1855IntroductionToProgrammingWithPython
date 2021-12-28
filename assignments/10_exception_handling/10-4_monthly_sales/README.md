# Project 10-4: Monthly Sales
Add exception handling to a program that reads the sales for 12 months from a file and calculates the total yearly sales as well as the average monthly sales. If you’ve done project 9-4, you can add the excepti n handling to that program. Otherwise, you can start this program from scratch.
## Console
```
COMMAND MENU
monthly - View monthly sales
yearly - View yearly summary
edit - Edit sales for a month
exit - Exit program

Command: edit
Three-letter Month: Dec
Sales Amount: TK
Sales amount for Dec was modified.

Command: monthly
Jan - 14317
Feb - 3903
Mar - 1073
Apr - 3463
May - 2429
Jun - 4324
Jul - 9762
Aug - 15578
Sep - 2437
Oct - 6735
Nov - 88
Dec - TK

Command: yearly
Using sales amount of 0 for Dec.
Yearly total: 64109
Monthly average: 5342.42

Command: exit
Bye!
```
## Specifications
- If the program can’t find the CSV file when it starts, display an error message and exit the program.
- For the edit command, display an error message if the user doesn’t enter a valid three-letter month abbreviation.