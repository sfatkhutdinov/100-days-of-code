# # FileNotFound
# try:
#     file = open('file.txt')
#     dictionary = {'key': 'value'}
#     print(dictionary['asdfadf'])
# except FileNotFoundError:
#     file = open('file.txt', 'w')
#     file.write('something')
# except KeyError as error_message:
#     print(f'The key {error_message} does not exist.')
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError('The is an error i made up')

height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height should not be over 3 meters')

bmi = weight / height ** 2
print(bmi)