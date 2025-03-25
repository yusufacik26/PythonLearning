import pandas as pd
import numpy as np

personeller = {
    'Çalışanlar': ['Ahmet Yılmaz', 'Can Ertürk', 'Hasan Korkmaz', 'Cenk Saymaz', 'Ali Açık', 'Rıza Ertürk', 'Mustafa Can'],
    'Departman': ['İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'İnsan Kaynakları', 'Bilgi İşlem', 'Muhasebe', 'Bilgi İşlem'],
    'Yaş': [30, 25, 45, 50, 23, 34, 42],
    'Semt': ['Kadıköy', 'Tuzla', 'Maltepe', 'Tuzla', 'Maltepe', 'Tuzla', 'Kadıköy'],
    'Maaş': [5000, 3000, 4000, 2000, 8000, 4300, 4556]
}


df = pd.DataFrame(personeller)

result = df['Maaş'].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

semtler = df.groupby("Semt")
"""
for name, group in semtler:
    print(name) semtlerde çalışan kişilerin isimlerini verecek şekilde
    print(group)
    
    """


"""for name, group in df.groupby("Departman"):
    # Departmana göre isim verir

    print(name)
    print(group)
print(result)
"""

#result = df.groupby("Semt").get_group("Kadıköy")

# Departman olarak bilgi işlemdeki kişilerin bilgilerini verir
#result = df.groupby("Departman").get_group("Bilgi İşlem")


#result = df.groupby("Departman").sum()

# Burada içinde number olan kolonları alarak ortalama hesapladık
result = df.groupby("Departman")[df.select_dtypes(include="number").columns].mean()

# departmana göre maaş ortalaması
result = df.groupby("Departman")["Maaş"].mean()

# semte göre yaş ortlaması
result = df.groupby("Semt")["Yaş"].mean()
#semte göre yaş sayısı
result = df.groupby("Semt")["Yaş"].count()

result = df.groupby("Departman")["Yaş"].max()

result = df.groupby("Departman")["Maaş"].min()

result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]

#numpy kullanarak ortalama alma işi
#result = df.groupby("Departman")[["Maaş","Yaş"]].agg(np.mean)

# toplam ortalama max ve min alan metod
result = df.groupby("Departman")["Maaş"].agg(["sum", "mean", "max", "min"]) #.loc["Muhasebe"] ekleyerek muhasebe 

print(result)
