class person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi oluşturuldu")
    
    def info(self):
        print(self.name, self.surname, self.age)


class student(person):
    def __init__(self, name, surname, age,number):
        super().__init__(name, surname, age)
        self.number = number
        print("student nesnesi oluşturuldu")

    def ortlama_Al(self):
        print(f"{self.number} numaralı öğrenci ortalaması alınıyor")

class teacher(person):
    def __init__(self, name, surname, age,branch):
        super().__init__(name, surname, age)  # Burada da aynı şekilde
        self.branch = branch
        print("teacher nesnesi oluşturuldu")
    def teach(self):
        print(f"{self.name} {self.surname} isimli öğretmen {self.branch} branş dersini veriyor")

p1 = person("yusuf", "açık", 20)
p1.info()

s1 = student("faruk", "acik", 23,12)
s1.info()

t1 = teacher("ahmet", "akın", 21,"Physics")
t1.info()
t1.teach()