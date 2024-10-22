def calculte(x):
    print(x * 2)


calculte(5)


def summer(arg1, arg2):
    print(arg1 + arg2)


summer(5, 3)

summer(arg2=4, arg1=32)


def topla(arg1, arg2):
    """

    Parameters
    ----------
    arg1
    arg2

    Returns
    -------

    """

    print(arg1 + arg2)


def carp(a, b):
    x = a * b
    print(x)


carp(1, 2)



# girilen değeri bir liste içinde tutacak fonksiyon


list_store = []


def add(a):

    list_store.append(a * 2)
    print(list_store)



add(4)
add(3)
add(2)
add(1)



### Ön tanımlı fonksiyonlar




def say_hi(string = "yusuf"):
    print(string)
    print("hi")
    print("dude")



#say_hi()

def calculator(a,b,c,d):
    return int(a+b+c+d)


"""
def allCalculator(a,b,c,d):
    x = calculator(a,b,c,d)
    y = a*b*c*d

    print(x * y)




allCalculator(1, 2, 3, 4)

"""


adamlar = ["yusuf","emin","emir","hamza"]


for i in adamlar:
    print(i)