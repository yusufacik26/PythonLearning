sayilar = [2,1,3,4,6,7]
harfler = ["a","b","c","d","a"]


#minimum ve maksimum değerleri bulur bu harflerde de aynıdır
sonuc = min(sayilar)
sonuc2 = max(harfler)
print(sonuc)
print(sonuc2)


# ekleme kısmı

sayilar.append(31)
harfler.append("z")

#EKLEMEK İSTEDİĞİN DEĞERİN YERİNİ DE BELİRTEREK EKLERSEN İNSERT
sayilar.insert(3,7)



#silme
sayilar.pop() #listenin sonundaki değeri siler
harfler.remove("b")





#sıralama 
sayilar.sort() #harflerde de alfabetik ilerler

harfler.reverse()


print(harfler)
print(sayilar)

print(harfler.count("a")) # ARANAN DEĞERİN KAÇ TANE OLDUĞUNU BULURUZ

harfler.clear() # BURADA LİSTEYİ TAMAMEN SİLERİZ
print(sayilar.index(4))

