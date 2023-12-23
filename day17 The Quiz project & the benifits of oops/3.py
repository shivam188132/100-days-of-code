class User:
    def __init__(self, user_id, username):
        self.id= user_id
        self.name=username
        


user_1=User("001", "shivam")
user_2= User("002", "rider billa")

print(f"{user_1.name} and {user_2.name}")
print(f"{user_1.id} and {user_2.id}")