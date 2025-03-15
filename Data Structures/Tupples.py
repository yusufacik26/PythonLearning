# Tuples are instantiated with parentheses.
fullname = ('Masha', 'Z', 'Hopper')

# Tuples are immutable, so their elements cannot be overwritten.

print(fullname)

# You can combine tuples using addition.
fullname = fullname + ('Jr',)
print(fullname)

# The tuple() function converts an object's data type to tuple.
fullname = ['Masha', 'Z', 'Hopper']
fullname = tuple(fullname)
print(fullname)

def to_dollars_cents(price):
    '''
    Split price (float) into dollars and cents.
    '''
    dollars = int(price // 1)
    cents = round(price % 1 * 100)

    return dollars, cents

print(to_dollars_cents(13.32))

# "Unpacking" a tuple allows a tuple's elements to be assigned to variables.
dollars, cents = to_dollars_cents(6.55)
print(dollars + 1)
print(cents + 13)


# The data type of an element of an unpacked tuple is not necessarily a tuple.
print(type(dollars))


team = [('Marta', 20, 'center'),
        ('Ana', 22, 'point guard'),
        ('Gabi', 22, 'shooting guard'),
        ('Luz', 21, 'power forward'),
        ('Lorena', 19, 'small forward'),
        ]

print()
for name,age,position in team:
    print(name)

print()
for player in team:
    print(player[0])



# Fermuar görevi görerek iki değeri eşleştirmeyi sağlar
cities =['Paris','Wien','Istanbul']
countries = ['France','Austuria','Turkey']

places = zip(cities,countries)

print(list(places))

#Unzipping işlemi iki değeri ayırmamızı sağlar diyelim buraya da örnek daha açıklayıcı

scientist = [('Nikola','Tesla'),('Charles', 'Darwin'), ('Marie', 'Curie')]

given_names,surnames = zip(*scientist)

print(given_names)
print(surnames)


#enumerate() zip() işlevine benzer şekilde, indis ve eleman çiftleri üreten bir yineleyici döndürür.

letters = ['a', 'b', 'c','d','e']
for index, letter in enumerate(letters):
   print(index, letter)


#indexsin başlangıç değeri sıfırdır letters,2 dediğin zaman ama 2den başlar

