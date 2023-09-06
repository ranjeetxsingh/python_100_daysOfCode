import pandas

data = pandas.read_csv(r"nato_phonetic_alphabet.csv")

nato_dict = {value.letter: value.code for (key, value) in data.iterrows()}

word = input("Enter a word: ").upper()

nato_list = []

for letter in word:
    nato_list.append(nato_dict[f"{letter}"])

print(nato_list)
