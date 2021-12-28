# Assignment 5
## Project 5-2: Tip Calculator
Create a program that calculates three options for an appropriate tip to leave after a meal at a restaurant.
### Console
```
Tip Calculator

Cost of meal: 52.31

15%
Tip amount:   7.85
Total amount: 60.16

20%
Tip amount:   10.46
Total amount: 62.77

25%
Tip amount:   13.08
Total amount: 65.39
```
### Specifications
- The program should calculate and display the cost of tipping at 15%, 20%, or 25%.
- Assume the user will enter valid data.
- The program should round results to a maximum of two decimal places.
---
## Project 5-3: Change Calculator
Create a program that calculates the coins needed to make change for the specified number of cents.
### Console
```
Change Calculator

Enter number of cents (0-99): 99

Quarters: 3
Dimes:    2
Nickels:  0
Pennies:  4

Continue? (y/n): y

Enter number of cents (0-99): 55

Quarters: 2
Dimes:    0
Nickels:  1
Pennies:  0

Continue? (y/n): n

Bye!
```
### Specifications
- The program should display the minimum number of quarters, dimes, nickels, and pennies that one needs to make up the specified number of cents.
- Assume that the user will enter a valid integer for the number of cents.
- The program should continue only if the user enters “y” or “Y” to continue.
---
## Project 5-4: Shipping Calculator
Create a program that calculates the total cost of an order including shipping.
### Console
```
==============================================================
Shipping Calculator
==============================================================
Cost of items ordered: 49.99
Shipping cost: 7.95
Total cost: 57.94
Continue? (y/n): y
==============================================================
Cost of items ordered: -65.50
You must enter a positive number. Please try again.
Cost of items ordered: 65.50
Shipping cost: 9.95
Total cost: 75.45
Continue? (y/n): n
==============================================================
Bye!
```
### Specifications
- Use the following table to calculate shipping cost:
```
COST OF ITEMS SHIPPING COST
==============================================================
< 30.00 5.95
30.00-49.99 7.95
50.00-74.99 9.95
> 75.00 FREE
```
- If the user enters a number that’s less than zero, display an error message and give the user a chance to enter the number again.
---
## Project 5-5: Table of Powers
Create a program that displays a table of squares and cubes for the specified range of numbers.
### Console
```
Table of Powers

Start number: 90
Stop number:  100

Number    Squared    Cubed
======    =======    =====
90 8100   729000
91 8281   753571
92 8464   778688
93 8649   804357
94 8836   830584
95 9025   857375
96 9216   884736
97 9409   912673
98 9604   941192
99 9801   970299
10010000  1000000
```
### Specifications
- The formulas for calculating squares and cubes are:
```
square = x ** 2
cube = x ** 3
```
- Use tabs to align the columns.
- Assume that the user will enter valid integers.
- Make sure the user enters a start integer that’s less than the stop integer. If the user enters a start integer that’s greater than the stop integer, display an error message and give the user a chance to enter the integers again.