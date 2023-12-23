
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
phanetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phanetic_dict)
word = input("enter the word \n").upper()
word_list = [phanetic_dict[item] for item in word]
print(word_list)