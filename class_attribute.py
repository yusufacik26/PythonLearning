
class User:

    activeUsers = 0 

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

user1 = User("ysfack","yusuf","açık","20")
user2 = User("zhrnr","zehra","yılmaz","21")
user3 = User("emnkck","emin","koçak","20")

print(f"aktif kullanıcı sayısı {User.activeUsers}")

print(user2.logOut())

print(f"aktif kullanıcı sayısı {User.activeUsers}")