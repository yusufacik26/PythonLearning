
"""sayi = int(input("sayi giriniz"))

if(sayi > 0):
    if(sayi % 2 ==1):
        print("girilen sayi pozitif tek sayidir")
    else:
        print("girilen sayi pozitif fakat çift sayidir") 
else:
    print("girilen sayı negatiftir")       """ 


"""
#UYGULAMA2
x = int(input("x sayi girin "))
y = int(input("y sayi girin "))
z = int(input("z sayi girin "))


if(x > z) and (x > y):
    print("x en büyük sayi")

elif(y > x) and (y > z):
    print("y en büyük sayi")
else:
    print("z en büyük sayi")    
    """

# UYGULAMA 3

isim = input("isim giriniz: ")
yas = int(input("yaşınızı giriniz"))
egitim = input("eğitim seviyenizi girin")

if(yas >= 18):
    if(egitim =="lise") or (egitim =="üniversite"):
        print("ehliyet alabilirsiniz")
    else:
        print(f'{isim} ehliyet alamazsınız çünkü eğitim seviyeniz yetersiz')
else:
    print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor')           