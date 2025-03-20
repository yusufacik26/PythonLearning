import numpy as np


python_list = [1, 2, 3, 4, 5, 6]
np_array = np.array([1, 2, 3, 4, 5, 6])

print(type(python_list))
print(np_array)

python_multi = [[1, 2], [3, 4], [5, 6]]
np_array_multi = np_array.reshape(3, 2)
print(python_multi)
print(np_array_multi)

#kaç boyutlu olduğunu görmek için kullanılır
print (np_array_multi.ndim)


# kaç satır ve sütun olduğunu görmek için kullanılır

print(np_array_multi.shape)