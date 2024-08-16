
class Urun:
    def __init__(self,urunKodu,urunAdi,fiyati):

        self.urunKodu = urunKodu
        self.urunAdi = urunAdi
        self.fiyati = fiyati


    def __len__(self):
        return self.fiyati
    
    def __str__(self):
        return f"{self.urunKodu},{self.urunAdi},{self.fiyati} ürün listelendi"
    
    def __del__(self):
        print("ürün objesi silindi.")
    

urun1 = Urun("2321312","tv",5000)

print(len(urun1))
print(str(urun1))
del urun1