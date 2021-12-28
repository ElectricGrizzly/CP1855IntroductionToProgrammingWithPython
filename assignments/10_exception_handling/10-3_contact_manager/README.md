# Project 10-3: Contact Manager
Add exception handling to a program that manages the primary email address and phone number for a contact. If you’ve done project 9-3, you can add the exception handling to that program. Otherwise, you can start this program from scratch.
## Console if the contacts file is not found
```
Contact Manager
Could not find contacts file!
Starting new contacts file...

COMMAND MENU
list - Display all contacts
view - View a contact
add - Add a contact
del - Delete a contact
exit - Exit program

Command: list
There are no contacts in the list.

Command: add
Name: Mike Murach
Email: mike@murach.com
Phone: 559-123-4567
Mike Murach was added.

Command: list
1. Mike Murach

Command: view
Number: 2
Invalid contact number.

Command: view
Number: x
Invalid integer.

Command: view
Number: 1
Name: Mike Murach
Email: mike@murach.com
Phone: 559-123-4567

Command: exit
Bye!
```
## Specifications
- If the program can’t find the CSV fi le, it should display an appropriate message and create a new CSV file that doesn’t contain any contact data.
- For the view and del commands, display an appropriate error message if the user enters an invalid integer or an invalid contact number.
- When you add or delete a contact, the change should be saved to the CSV file immediately. That way, no changes are lost, even if the program crashes later.