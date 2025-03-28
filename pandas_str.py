import pandas as pd


data = pd.read_csv("nba.csv")

data.dropna(inplace= True)

#data["Name"] = data["Name"].str.upper()  # burda isimleri büyük harf yaptı

data["index"] = data["Name"].str.find('a')

data = data[data.Name.str.contains('Jordan')]

#data = data.Team.str.replace(' ','-')

data[['FirstName','LastName']]=data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand = True)

print(data.head(10))
