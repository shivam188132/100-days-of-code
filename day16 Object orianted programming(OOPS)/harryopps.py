class Person:
    name = "Harry"
    occupation= "Softwere devloper"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a= Person()
# b=Person()
# a.name="shubham"
# print(a.name)
#print(a.occupation)
a.info()