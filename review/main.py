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

#data = pd.read_csv('weather_data.csv')
#
# print(data['temp'].max())

# get data with row
#print(data[data.day == 'Monday'])
#print(data[data.temp == data.temp.max()])

#
# monday = data[data.day == 'Monday']
# monday_temp = monday.temp

## Create a dataframe from scratch
# data_dict = {
#     "student": ["Amy", "James", "Angela"],
#     "score": [79,87,98]
# }
# data = pd.DataFrame(data_dict)
#
# ##change to csv data
#
# data.to_csv('new_data.csv')
# print(data)

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

all_colors = len(data[data['Primary Fur Color'] == 'Black'])

black_fur_color  = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_fur_color  = len(data[data['Primary Fur Color'] == 'Cinnamon'])
gray_fur_color  = len(data[data['Primary Fur Color'] == 'Gray'])

data_dict = {
    "Fur color": ['black', 'gray', 'cinnamon'],
    "Count": [black_fur_color,gray_fur_color, cinnamon_fur_color],

}
new_data = pd.DataFrame(data_dict)

#new_data.to_csv('squirrel_count.csv')