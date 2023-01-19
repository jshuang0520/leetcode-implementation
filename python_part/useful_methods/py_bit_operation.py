from collections import defaultdict


print('---------------------------------------------------------------------------------------------\n')


google_str = 'python count bit 1 of integer'
print(f'google: {google_str}')
# https://stackoverflow.com/questions/9829578/fast-way-of-counting-non-zero-bits-in-positive-integer

for i in range(0, 10):
    print(f'num_wise: {i}, bit_wise (str expression): {bin(i)}')

"""
bin(n).count("1")
"""
dd = defaultdict(list)
for x in [1,2,4,8, 3,5,6, 7, 10,100,1000,10000]:
    dd[bin(x).count("1")].append(x)
print(f'dd: {dd}')

print('---------------------------------------------------------------------------------------------\n')