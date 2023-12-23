try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
     # print("There was an error")
    file =open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"That key {error_message}does not exists")

else:
    content = file.read()
    print(content)

# finally:
    # file.close()
    # print("file was closed")
    # raise TypeError("This is an error that i made up")
    # raise KeyError


height = float(input("Height: "))
weight = float(input("Weight: "))

if height>3:
    raise ValueError("Human height should not be over 3 meters.")


bmi = weight/ height**2

print(bmi)