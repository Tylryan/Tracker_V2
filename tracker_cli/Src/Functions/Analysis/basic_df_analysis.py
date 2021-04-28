#!/usr/bin/python3

import tracker_cli.Src.Functions.preprocessing as preprocessing
# historical_records = json_to_user_dataframe('../UserData/records.json')


def hours_by_subject(historical_records):
    df = preprocessing.json_to_user_dataframe(historical_records)[1]
    # Grouping the data by subject and summing the hours. Then turning that into a dataframe.
    total_hours_df = df.groupby('Subject').Hours.sum()
    # Renaming the column to "Hours Studied"
    total_hours_df.columns = ['Total']
    # Showing the user how many hours they studied each subject
    # Pausing the screen to let the user digest the information. Allows them to continue at their own pace.
    return total_hours_df


if __name__ == '__main__':
    print('Printing from history_analysis.py')
