import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve environment variables
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Check if environment variables are loaded
if not all([SMTP_ADDRESS, EMAIL, PASSWORD]):
    raise ValueError("Please check your .env file. Some environment variables are missing.")

# URL of the product page
URL = 'https://appbrewery.github.io/instant_pot/'

# Headers to mimic a real browser request
headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
}

# Send a GET request to the URL
response = requests.get(url=URL, headers=headers)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the price
price = float(soup.find(name='span', class_='aok-offscreen').getText().split("$")[1])

# Extract the product title and remove extra spaces
msg = str(soup.find(name='span', class_='product-title-word-break').getText()).replace(' ', '')

# Print the product title
print(msg)

#Check if the price is below the threshold
if price < 100:
    # Create the email message
    subject = "Amazon Price Alert!"
    body = f"{msg}, 10 Programs now £{price}\n{URL}"

    # Encode the message in UTF-8
    email_message = f"Subject: {subject}\n\n{body}".encode('utf-8')

    # Send the email
    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="maranataa10@gmail.com",
            msg=email_message
        )