# Assignment 3
## Project 2-1: Student Registration
Create a program that allows a student to complete a registration form and displays a completion message that includes the user’s full name and a temporary password.
### Console
```
Registration Form

First name:    Eric
Last name:     Idle
Birth year:    1934

Welcome Eric Idle!
Your registration is complete.
Your temporary password is: Eric*1934
```
### Specifications
- The user’s full name consists of the user’s first name, a space, and the user’s last name.
- The temporary password consists of the user’s first name, an asterisk (*), and the user’s birth year.
- Assume the user will enter valid data.
---
## Project 2-2: Pay Check Calculator
Create a program that calculates a user’s weekly gross and take-home pay.
### Console
```
Pay Check Calculator

Hours Worked:    35
Hourly Pay Rate: 14.50

Gross Pay:       507.5
Tax Rate:        18%
Tax Amount:      91.35
Take Home Pay:   416.15
```
### Specifications
- The formula for calculating gross pay is: gross pay = hours worked * hourly rate.
- The formula for calculating tax amount is: tax amount = gross pay * (tax rate / 100).
- The formula for calculating take home pay is: take home pay = gross pay – tax amount.
- The tax rate should be 18%, but the program should store the tax rate in a variable so that you can easily change the tax rate later, just by changing the value that’s stored in the variable.
- The program should accept decimal entries like 35.5 and 14.25.
- Assume the user will enter valid data.
- The program should round the results to a maximum of two decimal places.
---
## Project 2-3: Price Comparison
Create a program that calculates a user’s weekly gross and take-home pay.
### Console
```
Price Comparison

Price of 64 oz size: 5.99
Price of 32 oz size: 3.50

Price per oz (64 oz): 0.09
Price per oz (32 oz): 0.11
```
### Specifications
- The formula for calculating price per ounce is: price per ounce = price / ounces
- Assume the user will enter valid data.
- The program should round the results to a maximum of two decimal places.
---
## Project 2-4: Travel Time Calculator
Create a program that calculates the estimated hours and minutes for a trip.
### Console
```
Travel Time Calculator

Enter miles: 200
Enter miles per hours: 65

Estimated travel time
Hours: 3
Minutes: 5
```
### Specifications
- The program should only accept integer entries like 200 and 65.
- Assume that the user will enter valid data.

**HINT:** Use integers with the integer division and modulus operators to get hours and minutes.