
sayilar = [1,43,56,23,12,44]

sonuc = sorted(sayilar)
print(sorted(sayilar))



araclar = [

    {"title":"Audi A4","price":400000},
    {"title":"Range Rover","price":800000},
    {"title":"Mercedes","price":900000},
]


sonuc = sorted(araclar, key=lambda arac : arac["price"])
print(sonuc)