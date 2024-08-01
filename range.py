"""r = range(10) # bu şekilde sadece son değerini de verebiliriz ya da (1,10 )direkt aralık
              # veredebilriiz. başlangıç değeri dahil ama bitiş değil
r = range(1,10)
r=range(5,20,2) # başlangıç yeri nereye kadar gideceği ve son olarak kaçar kaçar gideceği
sonuc = list(r)

print(sonuc)"""



for i in range(1,20,3):
    if(i % 2 != 1):
        print(i)