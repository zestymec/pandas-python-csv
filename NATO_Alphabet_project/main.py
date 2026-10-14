import pandas
df = pandas.read_csv("NATO_Alphabet_project/nato_phonetic_alphabet.csv")
csv_dict = {row.letter:row.code for (n, row) in df.iterrows()}
word = input("write any word here :").upper()
words_letter = [csv_dict[letter] for letter in word]
print(words_letter)

