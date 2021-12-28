# Project 9-2: Wizard Inventory
Create a program that keeps track of the items that a wizard can carry.
## Console
```
The Wizard Inventory program

COMMAND MENU
walk - Walk down the path
show - Show all items
drop - Drop an item
exit - Exit program

Command: walk
While walking down a path, you see a scroll of uncursing.
Do you want to grab it? (y/n): y
You picked up a scroll of uncursing.

Command: walk
While walking down a path, you see an unknown potion.
Do you want to grab it? (y/n): y
You can't carry any more items. Drop something first.

Command: show
1. a wooden staff
2. a scroll of invisibility
3. a crossbow
4. a scroll of uncursing

Command: drop
Number: 3
You dropped a crossbow.

Command: exit
Bye!
```
## Specifications
- When the user selects the walk command, the program should read the items from the file, randomly pick one, and give the user the option to grab it.
- Your program should create another file that stores the items that the wizard is carrying.
- Make sure to update this file every time the user grabs or drops an item.
- The wizard can only carry four items at a time.
- For the drop command, display an error message if the user enters an invalid number for the item.