import pandas
student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()

# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
NATO = {row.letter: row.code for (index, row) in student_data_frame.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user = input("Enter a word to get phonetic: ").upper()

code = [ NATO[code] for code in user]
print(f"\n{code}")


