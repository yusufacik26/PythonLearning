

yaslar = [7,15,17,27,36]

def yetiskinmi(x):
    if x<18:
        return False
    else: 
        return True
    
sonuc = list(filter(yetiskinmi,yaslar))    


#---------------------------------------
sayilar = [1,2,3,12,45,67]
sonuc = list(filter(lambda x: x%2 == 1 ,sayilar))

#---------------------------------------

isimler = ["ali","kemal","sinem","kaan","eray"]

sonuc3 = list(filter(lambda n: n[0]=="k",isimler))







#----------------------------------------
users = [
    
    {"username":"yusufacik","posts":[]},
    {"username":"ysf","posts":["post1","post2"]},
    {"username":"acik","posts":["post1"]}
    
    ]

secim = list(filter(lambda u: len(u["posts"])>0,users))
print(secim)