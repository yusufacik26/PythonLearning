
sayilar = [1,2,3,4,15,16,17,23]
sonuc = []


for sayi in sayilar:
    if(sayi % 2 == 0):
        sonuc.append(sayi)


print(sonuc)        


#BUNUN METOD HALİ ŞU

sonuc = [sayi for sayi in sayilar if sayi % 2 ==0 ]
sonuc = [sayi if sayi % 2==1 else "çift sayi"for sayi in sayilar]
print(sonuc)