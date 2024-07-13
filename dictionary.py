"""
sehirler = ["istanbul","izmir"]
plakalar = [34,35]


print(plakalar[sehirler.index("istanbul")])
print(plakalar[sehirler.index("izmir")])

KULLANIMI BU ŞEKİLDE 
plakalar = {"izmir":35,"istanbul":34}

plakalar["eskişehir"] = 26 EKLEMELER BU ŞEKİLDE YAPILIR
plakalar["bursa"] = 16

print(plakalar)
"""

urunler = {

100:{
    "urunAdi":"monitor",
    "urunAciklamasi":"16 inc",
    "urunFiyati":[300,400],
    "garantiSuresi":3,


},
101:{
    "urunAdi":"SSD",
    "urunAciklamasi":"256 GB",
    "urunFiyati":[1500,1770],
    "garantiSuresi":2,

},

}


sonuc = urunler[101]

fiyat = urunler[100]["urunFiyati"][1] + urunler[101]["urunFiyati"][1]
print(fiyat)
