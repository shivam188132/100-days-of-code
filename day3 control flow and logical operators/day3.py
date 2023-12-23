#if else statement
print("welcome to the rollar coaster ")
height =  int(input("enter your height  "))
if height >=120:
    print("you can ride the rollercoaster")

else:
    print ("you cannot ride the rollercoaster ")

#1


# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 ==0:
    print("This is an even number.")
else :
    print ("This is an odd number.")  

# 2 


print("welcome to the rollar coaster ")
height =  int(input("enter your height  "))
if height >=120:
    print("you can ride the rollercoaster")
    age = int(input("enter your age "))
    if age>=18:
        print("you have to pay $12 ")
    elif 12<=age<18:
        print("you have to pay $8")

    elif age <12:
        print("you have to pay $4")
       
      
else:
    print ("you cannot ride the rollercoaster ")

#3

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight/height**2)

if BMI<=18.5:
    print(f"Your BMI is {BMI}, You are underweight. ")
elif 18.5<BMI<=25:
    print(f"Your BMI is {BMI}, You have a normal weight. " )
elif 25<BMI<=30:
    print(f"Your BMI is {BMI}, You are slightly overweight. ")
elif 30<BMI<=35:
    print(f"Your BMI is {BMI}, You are obese. ")  
else : 
      print (f"Your BMI is {BMI}, You are clinically obese. ")

#4

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year %4 ==0:
    if year %100==0:

        if year %400 ==0:
            print("Leap year.")
        else:
            print("Not leap year.")    


            
        

    else:
            print("Leap year.")     
else:
    print("Not leap year. ")      

#5

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

# 6
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
if size=="S":
    bill+=15
    if add_pepperoni== "Y":
       bill+=2
    if extra_cheese=="Y":
       bill+=1 
elif size=="M":
    bill+=20
    if add_pepperoni== "Y":
       bill+=3
    if extra_cheese=="Y":
       bill+=1
elif size=="L":
    bill+=25
    if add_pepperoni== "Y":
       bill+=3
    if extra_cheese=="Y":
       bill+=1
print(f"Your final bill is: ${bill}")

#7

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = name1+name2
lower_names= combined_names.lower()
t=lower_names.count("t")
r=lower_names.count("r")
u=lower_names.count("u")
e=lower_names.count("e")
first_digit = t+r+u+e

l=lower_names.count("l")
o=lower_names.count("o")
v=lower_names.count("v")
e=lower_names.count("e")
second_digit=l+o+v+e

score=int(str(first_digit)+str(second_digit))

if (score<10) or (score>90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score>40) and (score<50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

#8
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')   
print("welcome to the treasure island . your mission is to find the treasure ")
direction= input("wherre you want to go left or right\n")
direction_lowercase= direction.lower()
if direction_lowercase== "left":
    print("congrats")
    a1= input(' "swim" or "wait"\n ' )
    a1_low=a1.lower()
    if a1_low=="wait":
        print("congrats")
        a2=input("which door?\n")
        a2_low=a2.lower()
        if a2_low=="yellow":
             print("you win")
        elif a2_low=="red":
            print("bounded by fire \n game over")
        elif a2_low=="blue":
            print("eaten by beast \n game over")
        else:
            print("gameover")
    else:
        print("game over")
else:
        print("game over")            
             

       


      









       













