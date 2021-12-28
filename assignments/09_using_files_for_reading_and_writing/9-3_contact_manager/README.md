# Project 9-3: Contact Manager
Create a program that a user can use to manage the primary email address and phone number for a contact.
## Console
```
Contact Manager

COMMAND MENU
list - Display all contacts
view - View a contact
add - Add a contact
del - Delete a contact
exit - Exit program

Command: list
1. Guido van Rossum
2. Eric Idle

Command: view
Number: 2
Name: Eric Idle
Email: eric@ericidle.com
Phone: +44 20 7946 0958

Command: add
Name: Mike Murach
Email: mike@murach.com
Phone: 559-123-4567
Mike Murach was added.

Command: list
1. Guido van Rossum
2. Eric Idle
3. Mike Murach

Command: exit
Bye!
```
## Specifications
- When the program starts, it should read the contacts from the CSV file.
- For the view and del commands, display an error message if the user enters an invalid contact number.
- When you add or delete a contact, the change should be saved to the CSV file immediately. That way, no changes are lost, even if the program crashes later.