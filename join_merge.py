import pandas as pd

"""customers = {
'CustomerId': [1,2,3,4],
'FirstName':["Ahmet","Ali","Hasan","Canan"],
'LastName':["Yılmaz","Korkmaz","Çelik","Toprak"]
}


orders ={ 
'OrderId':[10,11,12,13],
'CustomerId':[1,2,5,7],
'OrderDate':['2010-07-04','2010-09-04','2010-07-07','2012-03-04']

}

df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])

print(df_customers)
print(df_orders)


result = pd.merge(df_customers,df_orders,how = "inner")
result = pd.merge(df_customers,df_orders,how = "left")"""






customersA = {
'CustomerId': [1,2,3,4],
'FirstName':["Ahmet","Ali","Hasan","Canan"],
'LastName':["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
'CustomerId': [4,5,6,7],
'FirstName':["Yusuf","Emin","Burhan","Kerem"],
'LastName':["Açık","Koçak","Arıcı","Durak"]
}
df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
df_customerB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])



result = pd.concat([df_customersA,df_customerB],axis=1)

print(result)