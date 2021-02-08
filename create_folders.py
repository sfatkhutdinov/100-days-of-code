import os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


# for day in range(1, 101):
#     createFolder(f'./day-{day}/')
#     with open(f'./day-{day}/day_{day}.py', 'w') as file:
#         pass       

day = 38  # TODO: Change the date
createFolder(f'./day-{day}/')
with open(f'./day-{day}/day_{day}.py', 'w') as file:
    pass
# Creates a folder in the current directory called data
