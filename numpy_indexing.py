import numpy as np
numbers = np.array([1, 3, 5, 4, 52, 6, 7, 8, 9, 10])

#result = numbers[3]
#result = numbers[:5]

# result = numbers[::-1] diziyi sondan yazdırılmasını sağlar -1 yerine -2 falan verseydin 2şer 2şer verirdi
numbers2 = [[1,3,5],[2,3,4],[3,4,5],[4,5,5]]
numbers2_array = np.array(numbers2)
result = numbers2_array[:,0]

result = numbers2_array[:4, :4]


arr1 = np.arange(0,10)
# arr2 = arr1 referans kopyalama
arr2 = arr1.copy()
arr2[0] = 31
print(arr1)
print(arr2)
print(result)
