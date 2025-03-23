import pandas as pd 
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index=["A","B","C"], columns=["Column1","Column2","Column3"])


result = df

#result = df["Columns1"]

result = df.loc[:,"Column1"]
result = type(df.loc["A"])
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,:"Column2"]

result = df.loc["B":"C",:"Column3"]


result = df.iloc[2] # burada satırı alıyoruz

result = df.loc["A","Column3"]

print(df.drop("Column3",axis=1))
print(df)

#print(result)