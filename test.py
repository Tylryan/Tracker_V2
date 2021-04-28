#!usr/bin/python3

import json
import pandas as pd

# Creating a dicitonary in python
dictionary = {'Date': [], 'Subject': [], 'Hours': []}
print(dictionary)
date = '01/21/21'
dictionary['Date'].append(date)
dictionary['Subject'].append('python')
dictionary['Hours'].append(2)
# Export as json
jn = json.dumps(dictionary)
print(jn)
# loading it back in as a dictionary
new_dict = json.loads(jn)
print(new_dict)


# Turning it into a dataframe
df = pd.read_json(jn)
df.set_index('Date', inplace=True)
print(df)
