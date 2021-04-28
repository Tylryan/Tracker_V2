#!/usr/bin/python3

from Src.Functions.first_steps import file_checking, first_data_entry
from Src.Functions.preprocessing import clear_terminal, json_to_user_dataframe
from Src.Functions.saving_data import save_record, backup_record
import pandas as pd
import json
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
file_checking()  # Works as of 04/23/21
# Function that creates their first data
first_data_entry()  # Works as of 04/23/21

clear_terminal()
# Main Menu

# Create a function that.
# 1. Reads Json
# 2. Puts it into to dataframes.
#     - User DataFrame: Easier for the user to read.
#     - Computational DataFrame: Easier to do computations on
proceed = True
while proceed == True:
    print("""
    Enter in a record formatted like: Python 01/01/21 1.5 \n
    Or Type in a number below.

    (1) Stopwatch
    (2) Time Calculator
    (3) Tracked Subjects
    (4) Stats and Charts
    (5) Last 5 Entries
    (6) Backup Save
    (7) Remove Entry
    (8) Help

    **********************************************************************
    (9) To exit the program
    **********************************************************************
            """)
    # This should be an easy to read version of the dataframe.
    # It should not be what I do computations on
    # Don't use this in any computations
    user_dataframe, computation_df = json_to_user_dataframe(
        'Src/UserData/records.json')

    with open('Src/UserData/records.json') as f:
        historical_records = json.load(f)

    print(user_dataframe)
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
    elif len(first_input) > 3:
        print('\nYou have entered too many arguments.')
        print('The maximum number of arguments is 3.')
        input('Press "Enter" to continue')
        clear_terminal()
    # If the user inserts a subject, data, and time
    elif len(first_input) == 3:
        save_option = input('Would You like to save? [Y/n] ')
        if 'n' in save_option:
            print('Not Saving.')
            break
        else:
            save_record(first_input, historical_records)
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
