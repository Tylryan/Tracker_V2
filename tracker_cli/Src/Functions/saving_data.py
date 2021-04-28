#!/usr/bin/python3
import pandas as pd
import time
import json
import os
from Src.Functions.preprocessing import json_to_user_dataframe
################################ SAVING ########################################
# This is the initial save


def save_record(first_input, historical_records):
    subject, date, hours = first_input

    historical_records['Date'].append(date)
    historical_records['Subject'].append(subject)
    historical_records['Hours'].append(hours)
    with open('tracker_cli/Src/UserData/records.json', 'w') as fp:
        json.dump(historical_records, fp)
    print('Record Saved')
    # historical_records.to_json('Src/UserData/records.json')

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
    try:
        # If the user wants to backup their data, this is the backup save that saves to a file called "backup.csv"

        with open('tracker_cli/Src/UserData/backup_records.json', 'w') as fp:
            json.dump(historical_records, fp)

        # historical_records['Date'] = pd.to_datetime(
        #     historical_records['Date']).dt.date
        # historical_records.to_csv('backup.csv', sep=',', index=False)
        # historical_records.to_csv(
        #     '~/Documents/tracker_backup/backup_data.csv', sep=',', index=False)
        print('Your backup has been saved. ')
        time.sleep(1.0)
    except Exception as e:
        print(f'Error Message: {e}')
        print('saving_data.py: Backup has failed')
        input('Press "Enter" to continue ')
