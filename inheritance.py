#kalıtım konusu


class person():
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age

        print("person nesnesi oluşturuldu")
    def info(self):
        print(self.name,self.surname,self.age)



class student(person):
    pass                


class teacher(person):
    pass


p1 = person("yusuf","açık","20")
p1.info()

s1 = student("faruk","acik","20")




t1 = teacher("ahmet","akın","20")
