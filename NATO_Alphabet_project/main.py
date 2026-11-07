import pandas

df = pandas.read_csv("/Users/apple/umeraziz/pandas-python-csv/NATO_Alphabet_project/nato_phonetic_alphabet.csv")

csv_dict = {row.letter: row.code for (n, row) in df.iterrows()}

word = input("write any word here :").upper()

try:
    words_letter = [csv_dict[letter] for letter in word]
except KeyError:
    print("Sorry, only letters in the alphabet please.")
else:
    print(words_letter)