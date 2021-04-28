#!/usr/bin/python3
import pandas as pd
import time
import json
import os
################################ SAVING ########################################
# This is the initial save


def save_record(first_input, historical_records):
    subject, date, hours = first_input
    print('Before Appending Records\n')
    print(historical_records)
    historical_records['Date'].append(date)
    historical_records['Subject'].append(subject)
    historical_records['Hours'].append(hours)
    print('After\n')
    print(historical_records)
    with open('./Src/UserData/records.json', 'w') as fp:
        json.dump(historical_records, fp)

    # historical_records.to_json('Src/UserData/records.json')
    print('Json Version')

    # new_record = pd.DataFrame(
    #     {'Date': [date], 'Subject': [subject], 'Hours': [hours]})
    # # Updating the historical records to reflect the new entry
    # updated_historical_records = historical_records.append(
    #     new_record, ignore_index=True)
    # print(historical_records)
    # # This is the main save. Could be corrupted by faulty code.
    # updated_historical_records.to_json(
    #     'Src/UserData/records.json')
    input('Press Enter')
    ############################### Backup #########################################
# This is an independent backup save in case the original save gets messed up


def backup_record(historical_records):
    # This print statement helps verify that nothing went wrong with the code.
    print('These are the last ten records. If they look correct, then backup is safe.\n\n')
    historical_records = pd.read_csv(
        'records.csv', parse_dates=True, infer_datetime_format=True)
    historical_records['Date'] = pd.to_datetime(
        historical_records['Date']).dt.date
    print(historical_records.tail(10))
    # Asking the user if they would like to back up their files
    backup = input('\n\nWould You like to back this data up? [Y/n] ')
    # A conditional statement depending on the user's input
    if 'n' in backup.lower():
        # If the user doesn't want to backup their data, then this elif statement will be activated
        # Confirming to the user that their data has not been backed up
        print('\n\nBackup database has NOT been updated.')
        # This give the user time to digest the the message above
        time.sleep(1.5)
    else:
        try:
            # If the user wants to backup their data, this is the backup save that saves to a file called "backup.csv"
            historical_records['Date'] = pd.to_datetime(
                historical_records['Date']).dt.date
            historical_records.to_csv('backup.csv', sep=',', index=False)
            historical_records.to_csv(
                '~/Documents/tracker_backup/backup_data.csv', sep=',', index=False)
            print('Your backup has been saved. ')
            time.sleep(1.5)
        except TypeError and ValueError:
            print('You have entered an incorrect date ')
            cont = input('Press "Enter" to continue ')
