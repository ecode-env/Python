from datetime import datetime

import pandas as pd
import random

today  = datetime.now()
today_tuple  = (today.month, today.day)

data = pd.read_csv('birthdays.csv')


birthdays_dict = {(data_row['month'], data_row['day']): data_row for index, data_row in data.iterrows()}
print()
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()
        content.replace('[NAME]', F"{birthdays_person["name"]}")

