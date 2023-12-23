is_on = True

while is_on:
    print("Welcome to the roller coaster")
    height = int(input("enter your height: "))

    if height >=120:

        print('You can ride the rollercoaster')
        age = int(input("enter your AGE"))
        
        if age >=18:
            print("You have to pay $12 ")

        elif 12<= age <18:
            print("You have to pay $8")

        elif age < 12:
            print("You have to pay $4")

    else:
        print("You cannot ride the rollercoaster")
        
    a = input("You want to quit? Yes/No:  ")
    print()
    a.lower()
    if a == "yes":
        is_on = False
