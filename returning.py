
"""
def usAlma(number):
    # x = usALMA
    def inner(power):
        return number**power
    return inner



x = usAlma(2)
y= usAlma(3)

print(x(3))

print(y(4))
"""

def islem(islem_adi):

    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam    
    
    def carpma(*args):
        carpim *=1
        for i in args:
            carpim *= i
        return carpim
    
    if islem_adi == "toplam":
        return toplam
    if islem_adi == "carpma":
        return carpma
    


toplama = islem("toplam")

print(toplama(2,3,45,6))