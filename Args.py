#parametre sayısını bilmediğimiz durumlarda kullanılan işlem

sayilar = [12,32,26,76,90]



def topla(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc


print(topla(2,3,4,5,23))