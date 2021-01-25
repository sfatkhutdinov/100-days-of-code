import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
data_dict = {
    'Fur Color': ['gray', 'red', 'black'],
    'Count': [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
# fur_colors = data['Primary Fur Color'].to_list()
# gray = 0
# red = 0
# black = 0
# for color in fur_colors:
#     if color == 'Gray':
#         gray += 1
#     elif color == 'Black':
#         black += 1
#     elif color == 'Cinnamon':
#         red += 1
# data_dict = {
#     'Fur Color': ['gray', 'red', 'black'],
#     'count': [gray, red, black]
# }
# data1 = pandas.DataFrame(data_dict)
# data1.to_csv('squirrel_count.csv')

#
# # data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(type(data['temp']))
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data['temp'].to_list()
# # print(temp_list)
# #
# # average = data['temp'].mean()
# # print(average)
# #
# # max_value = data.temp.max()
# # print(max_value)
# #
# # print(data.condition)
#
# # print(data[data.temp == max_value])
# #
# # monday = data[data.day == 'Monday']
# # print(monday)
# # to_fahrenheit = (monday.temp * (9/5)) + 32
# # print(to_fahrenheit)
#
#
# # create dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
#
# # weather = []
# # with open('weather_data.csv', 'r') as file:
# #     for line in file.readlines():
# #         line.strip()
# #         weather.append(line)
# #
# # print(weather)
#
# # import csv
# #
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #
# # print(temperatures)
