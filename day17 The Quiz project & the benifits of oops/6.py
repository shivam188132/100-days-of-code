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
print(e1.name)
