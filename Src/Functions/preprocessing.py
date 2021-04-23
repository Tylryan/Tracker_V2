#!/usr/bin/python3
import pandas as pd
import os
# Json to simple user dataframe


def json_to_user_dataframe(file_location):
    df = pd.read_json(file_location)
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    return df

# dataframe to json
# Literally `df.to_json('file.json')`


def clear_terminal():
    # If the system is microsoft, then print to the terminal "cls". If the system is not microsoft, print to the terminal "clear"
    clear = os.system('cls' if os.name == 'nt' else 'clear')
    return clear
