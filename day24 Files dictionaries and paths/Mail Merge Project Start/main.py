PLACE_HOLDER = "[name]"



with open(".\Input\\Names\invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open(".\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER, name)
        with open(f".\Output\ReadyToSend\letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

















"""with open("..\Mail Merge Project Start\Input\Letters\starting_letter.txt", mode="r") as file:
    chu = file.read()
    print(chu)"""