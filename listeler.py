iller = ["eskisehir","ankara","izmir","bursa"]

print(iller[0:2])# belirli index arasındakileri gösterir
print(iller[-1]) # negatif olursa eğer sondan başlar


iller[1]="konya"
print(iller)

sonuc = len(iller)# liste içindeki eleman sayısı


# listeye eleman eklemesi yapar
yeniIller = iller +["erzurum"] 



#listeden eleman siler

del iller[1]

print(iller)