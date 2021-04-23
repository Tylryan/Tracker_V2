#!/usr/bin/python3

from Src.Functions.preprocessing import clear_terminal
import os
import time
import pandas as pd


def file_checking():
    clear_terminal()
    # Check to see if the correct csv files are in the directory

    # Gets all the files and directories in the current directory
    files_in_directory = [file for file in os.listdir(
        'Src/UserData/')]  # this works
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
            time.sleep(1)
            os.sys.exit()
        else:

            # This just tells the terminal (mac/linux)
            os.system('touch Src/UserData/records.json')
            os.system('touch Src/UserData/backup_records.json')
            # input('Press "Enter" to continue ')

##################################### Checking if there is any data in those files ##############################################################################


def first_data_entry():
    empty_records_file = os.stat("./Src/UserData/records.json").st_size == 0
    if empty_records_file == True:
        print('\n\nLet\'s enter in a new record')
        input('Press "Enter" to continue')
        # Create the column names "Subject","Date","Hours" in the empty records.csv.
        historical_data = pd.DataFrame(columns=['Subject', 'Date', 'Hours'])
        print('\n\nPlease use a space as the delimiter!!')
        subject, date, hours = input('\nType in the SUBJECT DATE and HOURS spent in this format\n\n'
                                     'Python 01/01/25 1.5: ').lower().split()

        # Creating the new dataframe.
        first_record = pd.DataFrame(
            {
                'Subject': [subject],
                'Date': [date],
                'Hours': [hours]
            }
        )
        # Appending the new record to the dataframe
        historical_data = historical_data.append(first_record)
        print(historical_data)
        historical_data.set_index('Date', inplace=True)
        print(historical_data)
        # Turning these dataframes into json files
        historical_data.to_json(
            './Src/UserData/records.json', orient="columns")
        historical_data.to_json(
            './Src/UserData/backup_records.json', orient="columns")


if __name__ == '__main__':
    print('Good for you mate')
