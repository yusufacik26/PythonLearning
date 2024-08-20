def selamlama(fn):
    def inner(ad):
        print("Programa hoş geldiniz")
        fn(ad)
        print("görüşmek üzere")
    return inner        



def gunaydin(ad):
    
    print("Günaydın "+ad)
    

def iyigunler(ad):
    
    print("iyi günler "+ad)
    

def iyiaksamlar(ad):
   
    print("İyi akşamlar "+ad)
        


g = selamlama(gunaydin)
g("yusuf")        