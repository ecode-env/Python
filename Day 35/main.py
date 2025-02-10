import requests


api_key = '007a9e0073b92ffca2a05e58bed8c638'
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

weather_params = {
    'lat': -3.119028,
    'lon': -60.021732,
    'appid': api_key,
    'cnt': 4
}
response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


will_rain = False
for hour_data in weather_data['list']:
    weather_code = hour_data['weather'][0]['id']
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    print('Bring un umbrela')




