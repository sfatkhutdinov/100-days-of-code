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

#Write your 1 line code 👇 below:

squared_numbers = [number**2 for number in numbers]

#Write your code 👆 above:

print(squared_numbers)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

#Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

#Write your code 👆 above:

print(result)