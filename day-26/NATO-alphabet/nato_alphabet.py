import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dictionary)


def generate_phonetics():
    user_word = input("Type in a word: ").upper()
    try:
        output = [phonetic_dictionary[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetics()
    else:
        print(output)


generate_phonetics()
