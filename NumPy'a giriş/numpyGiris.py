import numpy as np

list_a = [1,2,3]
list_b = [4,5,6]

list_c = []

for i in range(len(list_a)):
    list_c.append(list_a[i]*list_b[i])

print(list_c)


array_a = np.array(list_a)
array_b = np.array(list_b)
print(array_a*array_b)


#np.zeros() Bu, önceden sıfırlarla doldurulmuş belirlenmiş bir şekle sahip bir dizi oluşturur:

np.zeros((3,2))


#np.full()
#Bu da belirli bir değerle önceden doldurulmuş, belirlenmiş bir şekle sahip bir dizi oluşturur:

np.full((3,2), 5)


#ndarray.flatten()
#Bu, dizinin bir boyuta daraltılmış bir kopyasını döndürür.
array_2d = np.array([(1, 2, 3), (4, 5, 6)])
print(array_2d)
print()
array_2d.flatten()

# ndarray.reshape() verileri değiştirmeden veriye yeni şekil verir
array_2d.reshape(3, 2)


