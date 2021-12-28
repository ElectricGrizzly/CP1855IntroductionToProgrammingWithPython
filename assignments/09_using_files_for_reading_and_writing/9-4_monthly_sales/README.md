# Project 9-4: Monthly Sales
Create a program that reads the sales for 12 months from a file and calculates the total yearly sales as well as the average monthly sales. In addition, this program should let the user edit the sales for any month.
## Console
```
Contact Manager

COMMAND MENU
monthly - View monthly sales
yearly - View yearly summary
edit - Edit sales for a month
exit - Exit program

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
Dec - 2497

Command: yearly
Yearly total: 66606
Monthly average: 5550.5

Command: edit
Three-letter Month: Nov
Sales Amount: 8854
Sales amount for Nov was modified.

Command: exit
Bye!
```
## Specifications
- For the edit command, display an error message if the user doesn’t enter a valid three-letter abbreviation for the month.
- When the user edits the sales amount for a month, the data should be saved to the CSV file immediately. That way, no data is lost, even if the program crashes later.
- Round the results of the monthly average to a maximum of 2 decimal digits.