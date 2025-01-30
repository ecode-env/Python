# with open('weather-data.csv') as data_file:
#     data = data_file.readlines()
# print(data)
from itertools import count

# import csv
#
# with open('weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather-data.csv')
# print(data)
#print(data['temp'])


#data_dict = data.to_dict()
# print(data_dict)

# data_list = data['temp'].to_list()
# print(data_list)


# data_list = data['temp'].to_list()
# data_list_avg = sum(data_list) / len(data_list)
#
# print(data_list_avg)



#print(data['temp'].mean())


#print(data['temp'].max())

#print(data[data.day == 'Monday'])

#print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday['temp'])
#
# Fahrenheit = monday.temp[0] * 9/5 + 32
#
# print(Fahrenheit)



# data_dict = {
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [25, 30, 35],
#     "Score": [85, 90, 95]
# }
#
# df = pandas.DataFrame(data_dict)
#
# df.to_csv('new_data.csv')

# print(df)

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')


gray_squirrels_count  = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count  = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv('squirrel_count.csv')



