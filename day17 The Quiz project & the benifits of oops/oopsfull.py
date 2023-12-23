class Phone:
    def make_call(self):
        print("make a call")
    def play_game(self):
        print("play a game")

p1=Phone()
p1.make_call()
p1.play_game()


class Phone:
    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

    def make_call(self):
        print("make a call")

    def play_game(self):
        print("play a game")


p2 = Phone()
p2.set_color("blue")
p2.set_cost(300)
p2.show_color()
p2.show_cost()
p2.play_game()


# contructor
class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender

    def Employee_details(self):
        print("name", self.name)
        print("age", self.age)
        print("salary", self.salary)
        print("gender", self.gender)

e1= Employee("rajabilla", 21, 15000, "male")
e1.Employee_details()

# inheritance
class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage=mileage
        self.cost=cost

    def show_vehicle_details(self):
        print("milege of vehicle is", self.mileage)
        print("cost of vehicle is ", self.cost)
        print("i am a vehicle")

v1=Vehicle(50, 900)
v1.show_vehicle_details()

class Car(Vehicle):
    def show_car(self):
        print("i am a car")
c1=Car(50, 900)
c1.show_vehicle_details        
c1.show_car()

class Car(Vehicle):
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)
        self.tyres=tyres
        self.hp=hp

    def show_car_details(self):
        print("i am a car")
        print("numbers of tyres are", self.tyres)
        print("value of horse power is ", self.hp)

c1=Car(50, 1000, 4, 60)
c1.show_vehicle_details()  

# Multiple inheritance in python

class Parent1:
    def assign_string_one (self, str1):
        self.str1=str1

    def show_string_one(self):
        return self.str1

class Parent2:
    def assign_string_two(self, str2):
        self.str2=str2

    def show_string_two(self):
        return self.str2

class Child(Parent1, Parent2):
    def assign_string_three(self, str3):
        self.str3=str3

    def show_string_three(self):
        return self.str3

d1= Child()
d1.assign_string_one("shibam")
d1.assign_string_two("rider cruse")
d1.assign_string_three("king")           
d1.show_string_one()
d1.show_string_two()
d1.show_string_three()   

# Multi level inheritance

class Parent:
    def get_name(self, name):
        self.name=name
    def show_name(self):
        print(self.name)

class Child(Parent):
    def get_age(self, age):
        self.age=age
    
    def show_age(self):
        print(self.age)

class GrandChild(Child):
    def get_gender(self, gender):
        self.gender=gender

    def show_gender(self):
        print(self.gender)
gc=GrandChild()
gc.get_name("sisodia larchat")
gc.show_name()
gc.get_age(21)
gc.show_age()
gc.get_gender("kinnar")
gc.show_gender()