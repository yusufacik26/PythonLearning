
# global scope
a = "global değer"
def fn1():
    a = "local değer"
    print(a)



fn1()
print(a)

#-------------------------------------------------------------------


city = "eskişehir"


def changeCity(new_city):
    city = new_city
    print(city)


changeCity("bursa")
print(city)