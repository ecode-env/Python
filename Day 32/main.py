# import smtplib
#
#
# my_gmail = "eyobbmulugeta@gmail.com"
# password = 'ftgpfxwyebrazxdf'
#
# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_gmail, password=password)
# connection.sendmail(from_addr=my_gmail, to_addrs='maranataa10@gmail.com', msg='aloo')
# connection.close()



import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

my_birthday = dt.datetime(year=2002, month=12,day=1)
print(my_birthday)