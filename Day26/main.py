import pandas

nato_file = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in nato_file.iterrows()}

user_input = input("enter the word:")
nato_word = [nato_dict[letter.upper()] for letter in user_input if letter!= ' ']
print(nato_word)
