#!/usr/bin/python3

from preprocessing import clear_terminal
import os
import time
import pandas as pd


def file_checking():
    try:
        clear_terminal()
        # Check to see if the correct csv files are in the directory

        # Gets all the files and directories in the current directory
        files_in_directory = [file for file in os.listdir('.')]
        # Checks to see if "records.csv" is in the current directory
        no_record = False
        no_backup = False
        if 'records.json' not in files_in_directory:
            no_record = True
        # Checks to see if "backup.csv" is in the current directory
        if 'backup_records.json' not in files_in_directory:
            no_backup = True

        # Creates csv files if both are not there
        if (no_record == True) and (no_backup == True):  # Both yes and no work 2-19-21
            print('You have neither a records.json nor backup_records.json')
            new_files = input('I will create them for you if you want: [Y/n] ')
            if 'n' in new_files:
                print('No new files were created')
                print('You are now leaving this program')
                time.sleep(2)
                os.sys.exit()
            else:

                # This just tells the terminal (mac/linux)
                os.system('touch records.json')
                os.system('touch backup_records.json')
                # input('Press "Enter" to continue ')
    except:  # This try except loop doesn't work
        print('The File Checking Function is not working')

##################################### Checking if there is any data in those files ##############################################################################


def first_data_entry():
    empty_records_file = os.stat("records.json").st_size == 0
    if empty_records_file == True:
        print('You have no data in your records.json')
        print('Let\'s enter in a new record')
        input('Press "Enter" to continue')
        # Create the column names "Subject","Date","Hours" in the empty records.csv.
        historical_data = pd.DataFrame(columns=['Subject', 'Date', 'Hours'])
        print('Please use a space as the delimiter!!')
        subject, date, hours = input('Type in the SUBJECT, DATE, and HOURS spent in this format\n\n'
                                     'Python 01/01/25 1.5: ').lower().split()

        # Creating the new dataframe.
        new_record = pd.DataFrame(
            {
                'Subject': [subject],
                'Date': [date],
                'Hours': [hours]
            }
        )

        historical_data = historical_data.append(new_record)
        historical_data.to_json('records.csv')
        historical_data.to_json('backup.csv')


if __name__ == '__main__':
    file_checking()
    first_data_entry()
