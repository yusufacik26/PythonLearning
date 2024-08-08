sonuc = all([True,False,True])
sonuc = any([True,False,True])



#True and True => True => All()
#True or True => True => Any()


sayilar = [0,1,4,7,8,10,15]


sonuc1 = [bool(sayi) for sayi in sayilar]
sonuc2 = any([bool(sayi) for sayi in sayilar])

sonucc = all([bool(num) for num in sayilar if num % 2 == 1])
sonuc = any([sayi %2 ==0 for sayi in sayilar])
print(sonuc)
