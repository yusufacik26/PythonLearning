"""diller = ["python","java","c++"]

index = 0

for i in diller:
    print(f"{index+1}-{diller[index]}")
    index += 1 

diller = ["python","java","c++"]
obje = enumerate(diller)   """

diller = ["python","java","c++"]
"""
for i in enumerate(diller):
    
    print(i)"""

for index,value in enumerate(diller,1):
    print(f"{index}-{value}")