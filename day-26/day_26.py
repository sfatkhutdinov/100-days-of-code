numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

name1 = "Stanislav"
letter_list = [letter for letter in name1]
print(letter_list)

new_range = [new_range * 2 for new_range in range(1, 5)]
print(new_range)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [number ** 2 for number in numbers]

# Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

# Write your code 👆 above:

print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
result = {word: len(word) for word in sentence.split()}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:


weather_f = {day: ((temp * 9 / 5) + 32) for (day, temp) in weather_c.items()}

print(weather_f)

# pandas has a similar function with iterrow()
