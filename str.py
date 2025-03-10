"""
str.join()
Yinelenebilir dizelerin birleştirilmesi olan bir dize döndürür.
Öğeler arasındaki ayırıcı, bu yöntemi sağlayan dizedir.
"""



separator_string = ' '
iterable_of_strings = ['Happy', 'birthday', 'to', 'you']

separator_string.join(iterable_of_strings)



"""
str.partition(sep)
Dizeyi ilk oluşumunda bölün ve ayır sep ıcıdan önceki parçayı, ayırıcının kendisini ve ayırıcıdan sonraki parçayı içeren bir 3 külü döndürün.
Ayırıcı bulunamazsa, dizgenin kendisini içeren bir 3 tuple ve ardından iki boş dizge döndürün.

"""

my_string = 'https://www.google.com/'

my_string.partition('.')




# Sample valid URL for reference while writing your function:
url = 'https://exampleURL1.com/r626c36'

### YOUR CODE HERE ###
def url_checker(url):
    url = url.split('/')
    protocol = url[0]
    store_id = url[-1]
    # If both protocol and store_id bad
    if protocol != 'https:' and len(store_id) != 7:
        print(f'{protocol} is an invalid protocol.',
            f'\n{store_id} is an invalid store ID.')
    # If just protocol bad
    elif protocol != 'https:':
        print(f'{protocol} is an invalid protocol.')
    # If just store_id bad
    elif len(store_id) != 7:
        print(f'{store_id} is an invalid store ID.')
    # If all ok
    else:
        return store_id