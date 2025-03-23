import pandas as pd 
import numpy as np
# data
numbers = [1,2,3,4,5]
letters = ['a','b','c']
dict = {'a':10,'b':20,'c':30}

random_numbers = np.random.randint(10,100,6)
#pandas_series = pd.Series()

#pandas_series = pd.Series(numbers)

#pandas_series = pd.Series(letters)

#pandas_series = pd.Series(5,[1,2,3,4]) soldaki liste index değerlerini atar otomatik

#pandas_series = pd.Series(5,['a','b','c'])

#pandas_series = pd.Series(dict) 
 
#pandas_series = pd.Series(random_numbers)

pandas_series = pd.Series([20,30,40,53],['a','b','c','d'])

#result = pandas_series[-2:]

result = pandas_series.ndim # boyut

result = pandas_series.shape # kaç elemanlı
result = pandas_series.dtype

result = pandas_series.max()

result = pandas_series+ pandas_series

result = pandas_series[pandas_series % 2 ==0]
result = pandas_series % 2 == 0
print(pandas_series)
print(pandas_series[pandas_series % 2 ==0])
print(result)



opel2018 = pd.Series([20,30,40],["astra","vectra","mokka"])
opel2019 = pd.Series([10,40,70],["astra","vectra","Grandland"])

total = opel2018 + opel2019
print(total)
print(total["astra"])