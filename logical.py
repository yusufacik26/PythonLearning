# AND operatörü veya


x = 15
#sonuc = 10 < x <20 bunu kullanmak yerine

sonuc =(x > 10) and (x < 20)
# Bunu kullanırız
# logik kapıları düşün mantık konusu gibi 

 



 # or operatörü (veya)
 # yine mantıktaki gibi ikisinden biri true olması yeter
sonuc =(x < 10 ) or (x % 3 == 0)



#Not operatörü sonuc neyse tam tersi yapar
karne_notu = 90
devamsizlik = 4
sonuc = not(x > 0) 


ceza_bilgisi = False

sonuc = (karne_notu >= 85) and (devamsizlik <10 )and(ceza_bilgisi==False)

print(sonuc)