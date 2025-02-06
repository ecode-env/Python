import smtplib
from datetime import datetime

import pandas as pd
import random

today  = datetime.now()
today_tuple  = (today.month, today.day)
data = pd.read_csv('birthdays.csv')

my_gmail = 'eyobbmulugeta@gmail.com'
password = 'ftgpfxwyebrazxdf'

birthdays_dict = {(data_row['month'], data_row['day']): data_row for index, data_row in data.iterrows()}
print()
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace('[NAME]', birthdays_person["name"])
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail ,to_addrs=birthdays_person['email'], msg=f"Subject:Happy Birthday\n\n{content}")

