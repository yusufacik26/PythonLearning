

class User:

    activeUsers = 0 


    @classmethod
    def display_active_users(cls):
        return f"{cls.activeUsers} tane aktif kullanıcı var"
    
    @classmethod
    def from_string(cls,data_str):
      username,name,surname,age =data_str.split(",")
      return cls(username,name,surname,age)
    
    def __init__(self,username,name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.activeUsers += 1




    def username(self):
        return f"{self.username}"
    

    def logOut(self):
        User.activeUsers -= 1
        return f"{self.username} programdan çıkış yaptı"
    


print(f"aktif kullanıcı sayısı {User.activeUsers}")
"""
user1 = User("ysfack","yusuf","açık","20")
user2 = User("zhrnr","zehra","yılmaz","21")
user3 = User("emnkck","emin","koçak","20")

print(f"aktif kullanıcı sayısı {User.activeUsers}")

print(user2.logOut())
"""
user5 =User.from_string("ysfack","yusuf","acik","20")

print(User.activeUsers())