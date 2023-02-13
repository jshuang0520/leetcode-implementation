
print('---------------------------------------------------------------------------------------------\n')


google_str = 'python list repeat element n times'
print(f'google: {google_str}')
# https://stackoverflow.com/questions/3459098/create-list-of-single-item-repeated-n-times
"""
[e] * n
"""
print(['a'] * 3)


print('---------------------------------------------------------------------------------------------\n')


google_str = 'python list pop stack overflow'
print(f'google: {google_str}')
# https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
google_str = 'python dict del pop stack overflow'
print(f'google: {google_str}')
# https://stackoverflow.com/questions/5713218/best-method-to-delete-an-item-from-a-dict
print(f'''
--- by value ---
`remove` removes the first matching value

--- by index --- -> NOTICE. in python dict, there is similar usage
`del` removes the item at a specific index
`pop` removes the item at a specific index and returns it
''')
"""The effects of the three different methods to remove an element from a list:


--- by value ---

`remove` removes the first matching value, not a specific index:
>>> a = [0, 2, 3, 2]
>>> a.remove(2)
>>> a
[0, 3, 2]


--- by index --- -> NOTICE. in python dict, there is similar usage

`del` removes the item at a specific index:
# for python list
>>> a = [9, 8, 7, 6]
>>> del a[1]
>>> a
[9, 7, 6]

# for python dict
>>> a = dict({1: 9, 
              2: 8, 
              3: 7})
>>> del a[3]
>>> a
{1: 9, 
 2: 8}



`pop` removes the item at a specific index and returns it.
# for python list
>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]

# for python dict
>>> a = dict({1: 9, 
              2: 8, 
              3: 7})
>>> a[3]
7
>>> a.pop(3)
7
>>> a
{1: 9, 
 2: 8}
"""


print('---------------------------------------------------------------------------------------------\n')


google_str = 'python list __add__ __iadd__'
print(f'google: {google_str}')
# https://stackoverflow.com/questions/9766387/different-behaviour-for-list-iadd-and-list-add
print('''__iadd__ mutates the list, whereas __add__ returns a new list, as demonstrated.''')
"""
consider the following code:
>>> x = y = [1, 2, 3, 4]
>>> x += [4]              -------> for python list += means calling .__iadd__(), it mutates the original list (thus faster)
>>> x
[1, 2, 3, 4, 4]
>>> y
[1, 2, 3, 4, 4]


and then consider this:
>>> x = y = [1, 2, 3, 4]
>>> x = x + [4]           -------> for python list x = x + [4] means calling .__add__(), it returns a new list (thus slower)
>>> x
[1, 2, 3, 4, 4]
>>> y
[1, 2, 3, 4]
"""


print('---------------------------------------------------------------------------------------------\n')


google_str = 'python list insert by index stack overflow'
print(f'google: {google_str}')
# https://stackoverflow.com/questions/61697633/python-list-insert-with-index
print('''note.
list.insert(i, e) will insert the element e before the index i
a = [] # []
a.insert(2, '2') # ['2']
a.insert(5, '5') # ['2', '5']
a.insert(0, '0') # ['0', '2', '5']


list.insert(i, x)
  Insert an item at a given position. The first argument is the index of the element before which to insert, 
  so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).
''')
lst = [0, 1, 2, 3, 4, 5]
print(f'original list: {lst}')
lst.insert(0, 'insert_elem_by_index')
print(f'after insert: {lst}')
# original list: [0, 1, 2, 3, 4, 5]
# after insert: ['insert_elem_by_index', 0, 1, 2, 3, 4, 5]
