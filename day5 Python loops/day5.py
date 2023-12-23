str_inp= 'hello from ffddsf'
op= str_inp.split()
print(op)

#!
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height= 0
for height in student_heights:
    total_height+=height
  

number_of_students= 0
for student in student_heights:
    number_of_students+=1

average_height= total_height/number_of_students
print(round(average_height))   

# 2

#Write your code below this row 👇
sum=0
for number in range(2,101,2):
    
    sum+=number
print(sum)    

# 3

#Password Generator Project
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("welcome to the password generator")
nu_letters= int(input("enter the no. of letters you want in password \n"))
nu_numbers= int(input("enter the no. of numbers you want in password \n"))
nu_symbols= int(input("enter the no. of symbols you want in password \n"))
password_list=[]
for char in range(1, nu_numbers+1):
    password_list.append(random.choice(numbers))
   
for char in range(1, nu_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nu_symbols+1):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
print(password_list)
password=" "
for char in password_list:
    password=password+char 
print(f"your password is {password}")          