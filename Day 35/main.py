import requests


api_key = ''


parameter = {
    'lat': 9.033140,
    'lon': 38.750080,
    'appid': '007a9e0073b92ffca2a05e58bed8c638'
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameter)

data = response.json()

print(data)



