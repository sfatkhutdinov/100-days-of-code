
with open('day-26/day-26-3-exercise/file1.txt') as file1:
    list1 = [int(number) for number in file1.readlines()]

with open('day-26/day-26-3-exercise/file2.txt') as file2:
    list2 = [int(number) for number in file2.readlines()]

result = [number for number in list1 if number in list2]
# Write your code above 👆

print(result)


