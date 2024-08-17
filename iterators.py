
#iterable

#iterator


sayilar = [1,2,3,4,5]


#for i in sayilar:
 #   print(i)


iterator = iter(sayilar) 



while True:
    try:
        sayi = next(iterator)
        print(sayi)
    except StopIteration:
        break    