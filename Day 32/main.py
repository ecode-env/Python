import smtplib


my_gmail = "eyobbmulugeta@gmail.com"
password = 'ftgpfxwyebrazxdf'

connection = smtplib.SMTP('smtp.gmail.com')
connection.starttls()
connection.login(user=my_gmail, password=password)
connection.sendmail(from_addr=my_gmail, to_addrs='maranataa10@gmail.com', msg='aloo')
connection.close()