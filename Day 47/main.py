import requests
from bs4 import BeautifulSoup
import smtplib

PASSWORD = "ftgpfxwyebrazxdf"
EMAIL = "eyobbmulugeta@gmail.com"

URL = 'https://appbrewery.github.io/instant_pot/'

headers= {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Host": "httpbin.org",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Linux\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-67b09ebd-18596435288397dd65edf8c1"
  }


response = requests.get(url=URL, headers=headers)


soup = BeautifulSoup(response.text, 'html.parser')

price = float(soup.find(name='span', class_='aok-offscreen').getText().split("$")[1])

link = 'https://appbrewery.github.io/instant_pot/'
msg = str(soup.find(name='span', class_='product-title-word-break').getText()).replace(' ', '')

print(msg)

if price < 100:
    # Create the email message
    subject = "Amazon Price Alert!"
    body = f"{msg}, 10 Programs now £{price}\n{link}"

    # Encode the message in UTF-8
    email_message = f"Subject: {subject}\n\n{body}".encode('utf-8')

    # Send the email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="maranataa10@gmail.com",
            msg=email_message
        )