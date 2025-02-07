import datetime

import requests

MY_LAT = 8.980603
MY_LNG = 38.757759

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# print(longitude, latitude)


parameter = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameter)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = datetime.datetime.now().hour
print(time_now)

