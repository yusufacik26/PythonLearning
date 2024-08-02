"""isim = "yusuf"

for harf in isim:
    if(harf == "s"):
        break
    print(harf)
"""

"""
i  = 0

while(i<10):
    i += 1
    if(i==5):
        continue
    print(i)"""



toplam = 0
i = 0

while (i<100):
    i += 1
    if(i % 2 == 1):
        continue
    else:
        toplam = toplam + i


print(f'toplam:{toplam}')