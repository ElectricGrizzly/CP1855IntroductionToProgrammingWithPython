# Project 10-2: Wizard Inventory
Add exception handling to a program that keeps track of the inventory of items that a wizard can carry. If you’ve done project 9-2, you can add the exception handling to that program. Otherwise, you can start this program from scratch.
## Console if the program can't find the inventory file
```
The Wizard Inventory program

COMMAND MENU
walk - Walk down the path
show - Show all items
drop - Drop an item
exit - Exit program

Could not find inventory file!
Wizard is starting with no inventory.

Command: walk
While walking down a path, you see a crossbow.
Do you want to grab it? (y/n): y
You picked up a crossbow.

Command: show
1. a crossbow

Command: drop
Number: x
Invalid item number.

Command:
```
## The error message if the program can't find the items file
```
Could not find items file.
Exiting program. Bye!
```
## Specifications
- When the user selects the walk command, the program should randomly pick one of the items that were read from the text file and give the user the option to grab it.
- The current items that the wizard is carrying should be saved in an inventory file. Make sure to update this file every time the user grabs or drops an item.
- The wizard can only carry four items at a time. For the drop command, display an error message if the user enters an invalid integer or an integer that doesn’t correspond with an item.
- Handle all exceptions that might occur so that the user can’t cause the program to crash. If the all items file is missing, display an appropriate error message and exit the program.
- If the inventory file is missing, display an appropriate error message and continue with an empty inventory for the user. That way, the program will write a new inventory file when the user adds items to the inventory.