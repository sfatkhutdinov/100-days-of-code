df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dictionary)

user_word = input("Type in a word: ").upper()
output = [phonetic_dictionary[letter] for letter in user_word]
print(output)
