# with open('weather-data.csv') as data:
#     data_list = data.readlines()
# print(data_list)
import pandas
# import csv
# with open('weather-data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas as pd

#data = pd.read_csv('weather-data.csv')

#print(data)

## to change data to dictionary

# data_dict = data.to_dict()
#
# print(data_dict)

# to change the colum of data to list

# data_list = data['temp'].to_list()
#print(type(data_list)) ## series
#print(data_list)

## to calculate the average of colm temp

#temp_av = sum(data_list) / len(data_list)
#print(temp_av)

## to calculate maximum of number with series method

# data_max = data['temp'].max()
# print(data_max)

##to get data in columns

#print(data.day)

## to get data in row

#print(data[data.day == 'Monday'])
## to get the maximum value of temp row.
#print(data[data.temp == data.temp.max()])

## to get one item in the table

# monday = data[data.day == 'Monday']
# print(monday.condition)

## to change from Celsius to Fahrenheit.

# monday = data[data.day == 'Monday']
# temp_celsius = monday.temp[0]
# temp_fahrenheit = (temp_celsius * 9/5) + 32
# print(temp_fahrenheit)


## create data frame with pandas
#
# data_dict = {
#     'student' : ['eyob', 'angela', 'jack'],
#     'scores' : [70, 80, 60]
# }
# data_ = pandas.DataFrame(data_dict)
# print(data_)

##change top csv

#print(data_.to_csv())


#-------------------------------------


data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])

squirrel_fur_color = pd.DataFrame({
    'gray': [gray_squirrel],
    'red': [cinnamon_squirrel],
    'black': [black_squirrel]

})
squirrel_fur_color.to_csv('new_fur_color.csv')
