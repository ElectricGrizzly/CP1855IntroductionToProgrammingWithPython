# Project 8-2: Wizard Inventory
Create a program that keeps track of the items that a wizard can carry.
## Console
```
The Wizard Inventory program

COMMAND MENU
show - Show all items
grab - Grab an item
edit - Edit an item
drop - Drop an item
exit - Exit program

Command: show
1. wooden staff
2. wizard hat
3. cloth shoes

Command: grab
Name: potion of invisibility
potion of invisibility was added.

Command: grab
You can't carry any more items. Drop something first.

Command: show
1. wooden staff
2. wizard hat
3. cloth shoes
4. potion of invisibility

Command: edit
Number: 1

Updated name: magic wooden staff
Item number 1 was updated.

Command: drop
Number: 3
cloth shoes was dropped.

Command: exit

Bye!
```
## Specifications
- Use a list to store the items. Provide three starting items.
- The wizard can only carry four items at a time.
- For the edit and drop commands, display an error message if the user enters an invalid number for the item.
- When you exit the program, all changes that you made to the inventory are lost.