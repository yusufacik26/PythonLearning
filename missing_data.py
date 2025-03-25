import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df= pd.DataFrame(data,index = ['a','c','e','f','g'],columns=['column1','column2','column3']) 

df =df.reindex(['a','c','e','z','f','g','b','s']) #yeniden index değerleri ekledik ama başta atanmadığı için nan döndü

newColumn = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]



df["column4"] = newColumn

#df = df.drop("column1",axis=1) #burda da kolon sildik


#result = df
result = df["column1"].isnull().sum

result = df[df['column1'].isnull()]

#kolon1deki nanları verir
result = df[df['column1'].isnull()]["column1"]

# tamamen boş olmayan sütunları verir
result = df[df['column1'].notnull()]

result = df.dropna() # axis = 0 => satıra null olmayanları gösterir
result = df.dropna(axis= 1 ) #axis =  1 => sütuna

result = df.dropna(how ="all") # hepsi nansa göstermez


result = df.sum()
result = df.sum().sum()
result = df.size
result = df.isnull().sum()

def ortalama(df):
    adet = df.size - df.isnull().sum().sum()
    toplam = df.sum().sum()
    return toplam / adet


ort = ortalama(df)

# tüm kolonların ortalamasını aldık
result = df.fillna(value = ortalama(df))

print(result)