import requests
from bs4 import BeautifulSoup
import smtplib

PASSWORD = "ftgpfxwyebrazxdf"
EMAIL = "eyobbmulugeta@gmail.com"

URL = 'https://appbrewery.github.io/instant_pot/'

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}


response = requests.get(url=URL, headers=header)


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