# data types
# strings
# print("hello"[4])

num_char = len(input("what is your name? "))
new_num_char = str(num_char)
print("your name has " + new_num_char + "  characters")

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇
a= two_digit_number[0]
b= two_digit_number[1]
print(int(a)+int(b))

# print(3*3+3/3-3)
# print(3*(3+3)/3-3)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi= int(weight)/float(height)**2
print(int(bmi))

print (int(8/3))
print (round(8/3),2)

score =0
height=1.8
iswinning=True
#f-strin
# print(f"your score is {score}, your height is {height}, your winning is {iswinning}")'''
# print ("your score is ", str(score) + " your height is ", str(height) +"your winning is ", str(iswinning))

score =0
height=1.8
iswinning=True
print (f"your height {height} +  score {score}")

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_in_int= int(age)
your_age= 90 - age_in_int
days_1 = your_age*365
weeks_1 = your_age*52
months_1= your_age*12

print (f"You have {days_1} days  , {weeks_1}  weeks ,and {months_1} months left. ")

# project 2
print("welcome to the tip calculator")
a = input("what was the total bill ")
b = input("what percentage tio would you like to give ? 10,12, or 15 ?")
c = input("how many people want to split the bill ?")
tip = float(a) * float(b) / 100

total_bill = tip + float(a)

split_pay = total_bill / float(c)
print("every one have to pay", round(split_pay, 2))
