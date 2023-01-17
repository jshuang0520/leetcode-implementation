from collections import defaultdict

""" 'default_dict' - timing to use

e.g. python_part/array/1010-pairs-of-songs-with-total-durations-divisible-by-60.py

To solve such questions 
when we need to find number of pairs such that sum of multiply anything is divisible by any number 
the solution is ->     HASHMAP         +      MOD
                (find number of pairs)    (divisible)
                
"""

# reference

# python official site
# https://docs.python.org/3/library/collections.html#defaultdict-examples

# ---------------------------------------------------------------------------------

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)  # key, value 的 value -> data type 訂為 list
for k, v in s:
    d[k].append(v)

print(d)
"""
defaultdict(list, 
           {'yellow': [1, 3], 
            'blue': [2, 4], 
            'red': [1]
            })
"""
sorted(d.items())
"""[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]"""

# ---------------------------------------------------------------------------------

s = 'mississippi'
d = defaultdict(int)  # key, value 的 value -> data type 訂為 list
for k in s:
    d[k] += 1

print(d)
"""
defaultdict(int, 
            {'m': 1, 
            'i': 4, 
            's': 4, 
            'p': 2})
"""
sorted(d.items())
"""[('i', 4), ('m', 1), ('p', 2), ('s', 4)]"""

# ---------------------------------------------------------------------------------


# https://www.accelebrate.com/blog/using-defaultdict-python


food_list = 'spam spam spam spam spam spam eggs spam'.split()
food_count = defaultdict(int)  # default value of int is 0;  key, value 的 value -> data type 訂為 int
for food in food_list:
    food_count[food] += 1  # increment element's value by 1
"""
defaultdict(<type 'int'>, 
            {'eggs': 1, 
            'spam': 7
            })
"""


city_list = [('TX', 'Austin'), ('TX', 'Houston'), ('NY', 'Albany'), ('NY', 'Syracuse'), ('NY', 'Buffalo'),
             ('NY', 'Rochester'), ('TX', 'Dallas'), ('CA', 'Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]
cities_by_state = defaultdict(list)
for state, city in city_list:
    cities_by_state[state].append(city)  # cannot be defaultdict(tuple) cuz 'tuple' object has no attribute 'append'
"""
defaultdict(list,
            {'TX': ['Austin', 'Houston', 'Dallas'],
             'NY': ['Albany', 'Syracuse', 'Buffalo', 'Rochester'],
             'CA': ['Sacramento', 'Palo Alto'],
             'GA': ['Atlanta']
             })
"""
