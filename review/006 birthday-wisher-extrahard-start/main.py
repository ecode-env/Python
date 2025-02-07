from datetime import datetime
import random
import pandas
import smtplib


today = (datetime.now().month, datetime.now().weekday())

data = pandas.read_csv('birthdays.csv')

data_dict = {
    (row_data.month, row_data.day): row_data for index, row_data in data.iterrows()
}

my_gmail = 'eyobbmulugeta@gmail.com'
password = 'ftgpfxwyebrazxdf'

if today in data_dict:
    person = data_dict[today]
    path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(path) as letter_file:
        content = letter_file.read()
        content = content.replace('[NAME]', person['name'])
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(from_addr=my_gmail,to_addrs=person['email'], msg=f'Subject:Happy Birthday\n\n{content}')