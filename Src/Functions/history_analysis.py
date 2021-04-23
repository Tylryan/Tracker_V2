#!/usr/bin/python3

from preprocessing import json_to_user_dataframe
# historical_records = json_to_user_dataframe('../UserData/records.json')


def hours_by_subject(historical_records):

    # Grouping the data by subject and summing the hours. Then turning that into a dataframe.
    total_hours = historical_records.groupby('Subject').Hours.sum()
    # Renaming the column to "Hours Studied"
    total_hours.columns = ['Total']
    # Showing the user how many hours they studied each subject
    # Pausing the screen to let the user digest the information. Allows them to continue at their own pace.
    return total_hours


if __name__ == '__main__':
    print('Printing from history_analysis.py')
