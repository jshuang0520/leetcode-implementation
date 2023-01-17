
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
