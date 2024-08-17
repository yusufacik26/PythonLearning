
def sayac(max):
    sayi = 1 
    while sayi <= max:
        yield sayi 
        sayi +=1



iterator = sayac(20)




#for i in iterator:
 #   print(i)  

sonuc  = list(iterator)

print(sonuc)