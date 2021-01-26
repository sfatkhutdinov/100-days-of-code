student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dictionary)

user_word = input("Type in a word: ").upper()
output = [phonetic_dictionary[letter] for letter in user_word]
print(output)
