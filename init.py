
class Product():
    def __init__(self,name,price,isActive=True):
        
        self.name = name
        self.price = price
        self.isActive = isActive

        print("product nesnesi oluşturuldu")


p1 = Product("range rover","700000")
p2 = Product("BMW","400000",False)

print(p1.name,p1.price,p1.isActive)

print(p2.name,p2.price,p2.isActive)
