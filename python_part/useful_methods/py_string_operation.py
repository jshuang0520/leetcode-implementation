string = '7777'
string = string.replace('7', '')  # replace all occurrences
print(f'string: {string} \n')

string = '7777'
string = string.replace('7', '', 1)  # replace ONCE
print(f'string: {string} \n')

print('---------------------------------------------------------------------------------------------\n')

# to see if it is symmetric (palindrome)
if string + string[::-1] == string[::-1] + string:
    print('the string is symmetric (palindrome) \n')
