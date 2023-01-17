from collections import Counter

# reference
# https://docs.python.org/zh-tw/3/library/collections.html#counter-objects


print('---------------------------------------------------------------------------------------------')

print('notice the differences - list() vs []:\n')


print(Counter(list("balloon")))
"""
Counter({'l': 2, 'o': 2, 'b': 1, 'a': 1, 'n': 1})
because
list("balloon") == ['b', 'a', 'l', 'l', 'o', 'o', 'n']
"""
print(Counter(["balloon"]))
"""
Counter({'balloon': 1})
because
["balloon"] == ["balloon"]
"""

print('---------------------------------------------------------------------------------------------')

print('But usage of Counter is similar to dictionary. \n')


# method 1 (is equivalent to method 2)
print(Counter(['red', 'blue', 'red', 'green', 'blue', 'blue']))
"""
Counter({'blue': 3, 'red': 2, 'green': 1})
"""
# method 2 (is equivalent to method 1)
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(f'type(cnt): {type(cnt)}; cnt: {cnt}')
print(f'type(dict(cnt)): {type(dict(cnt))}; dict(cnt): {dict(cnt)}')
"""
Counter({'blue': 3, 'red': 2, 'green': 1})
"""
print(f"cnt['blue']: {cnt['blue']}")

print(f'''
cnt.elements(): {cnt.elements()}
list(cnt.elements()): {list(cnt.elements())}
sorted(cnt.elements()): {sorted(cnt.elements())}
''')
