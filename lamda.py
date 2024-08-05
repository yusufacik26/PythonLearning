
#lamba arguments : expression

sonuc = (lambda a : a**2)(3)




us_Alma = lambda a: a**2
sonuc = us_Alma(4)




#---------------------------
tersCevir = lambda x :x[::-1]

sonuc = tersCevir("Yusuf Acik")
print(sonuc)




#------LAMBDA FONKSİYON İÇİNDE KULLANIMI ------------------------------



def fn1(n):
    return lambda a: a**n

us_Alma2 =fn1(2)
sonuc = us_Alma2(3)
print(sonuc)








