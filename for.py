"""sayilar = [1,2,3,4,12,34,55,66,13]


for i in sayilar:
    print(i)



isimler = ["yusuf","acik","computer","engineer"]

for isim in isimler:
    print(isim)"""



"""_tuple = [(1,2),(3,4),(9,3)]

for x,y in _tuple:
    print(x,y)"""



iller = {"01":"ankara","02":"adana","03":"eskişehir"}

"""for i in iller:    
    print(iller[i])  burda isimler

for x in iller:  burda da plakalar var
    print(x)"""  


for i  in iller.values():
    print(i) #burda da isimler var



for key,value in iller.items():  #bu şekilde plaka ve şehir yan yana kullanılır
    print(key,value)