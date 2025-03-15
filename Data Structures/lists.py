x = ["Now", "We","Are","cooking","with",7,"ingrediendts"]


print(x[1:3])
print(type(x))


# The append() method adds an element to the end of a list. SONUNA EKLER
fruits = ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.append('Kiwi')
print(fruits)


#Insert ise index numarasının olduğu yere ekler

fruits.insert(2, 'Orange')
print(fruits)

#Remove() metodu silemeye yöneliktir

fruits.remove('Apple')
print(fruits)


#Liste işlemleri

num_list = [1, 2, 3]
char_list = ['a', 'b', 'c']
print(num_list+char_list)
#Bunun sonucunda iki liste toplanır

list_a = ['a', 'b', 'c']
print(list_a * 2)
#Listedeki değerler 2 tane olur artık Ancak bunlar çıkarılamaz veya bölünemez.


#in operatörünü kullanarak bir değerin bir listede yer alıp almadığını kontrol edebilirsiniz:

num_list = [1, 2, 3]

print(4 in num_list)
print(4 not in num_list)

#clear()
#Tüm öğeleri kaldırın:

my_list = ['a', 'b', 'c']
my_list.clear()
print(my_list)




# sort() Varsayılan olarak listeyi artan şekilde sıralar

char_list = ['s', 'z', 'c','a']
char_list.sort()
print(char_list)