#!/usr/bin/python3

# TODO
# 1. Use Json to store files, then pull them in as dataframes.
# 2. Create Classes as much as possible
# - Split Those Classes into separate files.
# - @static and @classmethods
# 3. Incorporate Decorations
# 4. Generators
# 5. x, y = func(a,b) This kind of thing.
# 6. List comprehensions
# - Turnary Operators.
# - Generators
# 7. if __name__ = '__main__'
# 8. Add color to the terminal outputs. (Green : Good, Red: Bad, Yellow: Warn)
# 9. Make a Cli tool that does things without having to actually open the
# program
# 10. Create a link between the main file and you bash script. This helps speed
# up the open time of the application.
# 11. Conditions = [
# a > b,
# c > b
# ]
# print(true) if conditions : else print(false)
# Really all in all, you want to fit as many tricks and cool concepts into
# this project. After all, this is just practice.

# Function that checks to make sure they have the right files


# Function that creates their first data


# Main Menu
print("""
Enter in a record formatted like: Python 01/01/21 1.5 \n
Or Type in a number below.

(1) Stopwatch
(2) Time Calculator
(3) Tracked Subjects
(4) Last 5 Entries
(5) Stats and Charts
(6) Backup Save
(7) Remove Entry
(8) Help

**********************************************************************
(9) To exit the program
**********************************************************************
        """)

# Create a function that.
# 1. Reads Json
# 2. Puts it into to dataframes.
#     - User DataFrame: Easier for the user to read.
#     - Computational DataFrame: Easier to do computations on
proceed = True
while proceed == True:
    first_input = input('What would you like to do? ').lower().split()
    user_choice = first_input[0]
    stop_conditions = [
        user_choice == '9',
        user_choice == 'stop',
        user_choice == 'exit',
        user_choice == 'quit'
    ]
    # Conditions that could stop the program
    # I labeled them stop conditions to reuse them later
    if any(stop_conditions):
        print('You are leaving the program')
        break
    # If the user inserts a subject, data, and time
    elif len(first_input) == 3:
        subject, date, hours = first_input
        print('You have entered in a subject, date, and time')

    # Stopwatch

    elif user_choice == '1':
        print('You have selected the stopwatch')

    elif user_choice == '2':
        print('You have chosen the time calculator')

    elif user_choice == '3':
        print('You have chosen to list the your tracked subjects')

    elif user_choice == '4':
        print('You have chosen to list your Stats and Charts')

    elif user_choice == '5':
        print('You have chosen to list your last 5 entries')

    elif user_choice == '6':
        print('You have chosen to Back up your data')

    elif user_choice == '7':
        print('You have chosen to Remove and Existing Entry')

    elif user_choice == '8':
        print('You have chosen to see the help menu')
