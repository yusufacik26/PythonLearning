def fullName(firstName,lastName):
    return f"Sisteme hoş geldiniz,{firstName} {lastName}"

sonuc = fullName("yusuf","acik")
sonuc = fullName("acik","yusuf") # burada şöyle bir sıkıntı var eğer ters girilirse isimler
                                 # çıktı da ters olur

sonuc = fullName(lastName="acik",firstName="yusuf") # üstteki sorun çözümü bu şekilde 
print(sonuc)