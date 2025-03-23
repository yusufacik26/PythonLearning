import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result = df

result = df.head(10) # head ile baştaki verileri yazarsın burda ilk 10 veri
result = df.tail() # son kısımdaki ilk 5 veri gelir

result = df["Column1"].head()

result = df[df%2 ==0 ]
result = df[(df["Column1"]>50) & (df["Column2"]<=70)]
result = df[(df["Column1"]>40)|(df["Column2"]<=70)]
print(result)