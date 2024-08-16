

class User:
    #yapıcı metod(constructer)

    def __init__(self,username,name,surname,birthday):

        #object attribute , instance attribute
        self.username= username
        self.name= name
        self.surname= surname
        self.birthday=birthday

    def info(self):
        return f"{self.username} kullanıcı adıyla {self.name},{self.surname},sisteme kaydedildi"   


u1 = User("lordSnow","yusuf","acik",2004)    
print(u1.info())