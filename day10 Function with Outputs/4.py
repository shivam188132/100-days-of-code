# add
import os
from art import logo
print(logo)
def calc():

    def add(n1, n2):
        return n1+n2
    def sub(n1, n2):
        return n1-n2
    def multiply(n1, n2):
        return n1*n2
    def divide(n1, n2):
        return n1/n2

    operations ={
        "+": add,
        "-": sub,
        "*": multiply,
        "/": divide}
    should_continue=True
    while should_continue:
        num1=float(input("enter the value of number first "))
        num2=float(input("enter the value of number second "))
        for items in operations:
            print(items)
        operation_symbol=input("pick a symbol above to do a operation  ")
        calculation_function=operations[operation_symbol]
        answer= calculation_function(num1, num2)
        print(f"{num1}  {operation_symbol}  {num2}= {answer}")
        num3=float(input("enter the third number  "))
        operation_symbol=input("pick the operation symbol  ")
        calculation_function=operations[operation_symbol]
        answer2=calculation_function(answer, num3)
        print(f"{answer}  {operation_symbol}  {num3}= {answer2}")
        a=input("want to run again type y or n   ")
        if a=="n":
            should_continue=False
            os.system('cls')
            calc()

calc()           