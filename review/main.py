# with open('weather_data.csv') as data:
#     print(data.readlines())

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd

data = pd.read_csv('weather_data.csv')

print(data['temp'].max())

# get data with row

print()
