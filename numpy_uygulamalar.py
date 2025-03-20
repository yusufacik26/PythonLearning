import numpy as np


"""np_array = np.array([10,15, 30, 45, 60])
print(np_array)


np_array = np.arange(5,15)
print(np_array)

5ten 15 kadar sayılar yazıyor


np_array = np.arange(50,100,5)
print(np_array)

np_array =np.zeros((10,10))
print(np_array)

np_array = np.ones(10)
print(np_array)

np_numbers = np.random.randint(0,100)
print(np_numbers)

np_numbers = np.random.randint(-1,1,10)
print(np_numbers)

hemde böyle yapılabilir
np_array = np.random.randint(10,50,15)
np_array_new = np_array.reshape(3,5)
print(np_array_new)


hem böyle 
matris = np.random.randint(10,50,15).reshape(3,5)
print(matris)



matris = np.random.randint(10,50,15).reshape(3,5)
print(matris)
print(matris.min())
print(matris.max())


np_array = np.arange(10,20)
print(np_array)
print(np_array[:3]) İLK 3 ELEMANI YAZDIRMA
print(np_array[::-1]) TERSTEN YAZDIRMA


matris = np.random.randint(10,20,15).reshape(5,3)
print(matris)

0.satır 2.sütundaki elemanı verir
print(matris[0:2])

print(matris[:, 0])
"""
# 0 dan büyük çift sayıları yazdırır
np_array = np.arange(-50,50,10)

ciftler = np_array[np_array % 2 == 0]
result = ciftler[ciftler >0]
print(result)
