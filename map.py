
sayilar = [1,2,3,4,5,6]
str_sayilar = [1,2,3,4,5,6]
karisik_sayilar = [2,-3,5,-6,8,-12]
kareleri = []


def kareAl(sayi):
    return sayi ** 2

sonuc2 = list(map(kareAl,sayilar))

sonuc = list(map(lambda sayi : sayi **2,sayilar))
sonuc = list(map(int,str_sayilar))
sonuc =list(map(abs,karisik_sayilar))

print(sonuc)
 