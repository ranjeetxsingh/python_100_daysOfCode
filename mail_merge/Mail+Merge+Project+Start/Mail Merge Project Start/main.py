
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.read()
    names_list = names.split('\n')


with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter = letter_file.read()

for name in names_list:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as personalized_letter:
        personalized_letter.write(letter.replace('[name]', name))
