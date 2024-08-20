
#kapsülleme
"""def dis_fonksyon(sayi1):
    print("dış fonksiyon çalıştı")
    def ic_fonksiyon(sayi1):
        print("ic fonksiyon çalıştı")
        return sayi1 ** 2
    sayi2 = ic_fonksiyon(sayi1)
    print(sayi1,sayi2)


dis_fonksyon(5)    
"""

def faktoriyel(number):
    if not isinstance(number,int):
        raise TypeError("giridğiniz değer tam sayı olmalıdır")
    def ic_faktoriyel(number):
        if number <= 1:
            return 1
        return number * ic_faktoriyel(number-1)
    return ic_faktoriyel(number)



print(faktoriyel(5))

