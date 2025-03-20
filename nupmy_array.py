import numpy as np

# result = np.array([1,2,3,4,5,6]) normal bir liste oluşturmamızı sağladık

# result = np.arange(1,11) başlangıç ve bitiş değeri olan liste oluşmasını sağladı

# result = np.arange(10,60,3)     başlangıç bitiş ve artış değeri sağladı

# result = np.zeros(10) verilen adet kadar olan 0  listesi verir

# result = np.ones(10)  verilen adet kadar olan 1 listesi verir

# result = np.linspace(0,100,5) [  0.  25.  50.  75. 100.] şeklinde parçalara ayrılmasını sağlar


# result = np.random.randint(0,2) başlangıç ve bitiş değeri olan rastgele sayı verir.
# result = np.random.randint(0,30,4) sondaki 4 kaç tane istediğini de yazıyor

np_array = np.arange(100)
np_multi = np_array.reshape(10, 10)

# print(np_multi.sum(axis = 1)) satırların toplamı

# print(np_multi.sum(axis = 0)) sütunların toplamı

rnd_numbers = np.random.randint(1,50,10)

#result = rnd_numbers.min()
# result = rnd_numbers.mean() ortalama almamzı sağlar

# result = rnd_numbers.argmax() en büyük sayının indisini verir
print(rnd_numbers)
print(result)
