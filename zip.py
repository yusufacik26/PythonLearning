liste1 = [1,2,3,4,5]
liste2 =["bir","iki","üç","dört","beş"]
liste3 = ["a","b","c","d","e"]

"""
sonuc = list(zip(liste1,liste2,liste3))

print(sonuc)"""


for x,y,z in zip(liste1,liste2,liste3):
    print(x,y,z)