class User:
    def __init__(self, user_id, username):
        self.id= user_id
        self.name=username
        self.followers=0
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

    def unfollow(self,user):
        user.followers-=1
        

m1=User("001", "shivam")
m2= User("002", "rider billa")

m1.follow(m2) 
m2.unfollow(m1)   
print(m1.followers)
print(m1.following)
print(m2.followers)
print(m2.following)