print(f'''summarize: to know better to concepts of:
1. algorithm with time complexity (str1 in str2 & matrix transpose)
2. class -> when it is initialized, instance, 'private member', and how to get a 'private member'
3. Difference between list() and creating a list through []
4. memory address -> the difference between using '==' and 'is'
''')

# ----------------------------------------------------------------
#
# question 1
#
# ----------------------------------------------------------------
""" restrictions:
1. can NOT use 'in'
2. can NOT use 'split'
3. can NOT use list operation
4. can use 'for' / 'while' loop

--
Input: m = "aaaaabaaaaabaaaaaa", s = "aaaaaa"
Output: True

Input: m = "abababababac", s = "abc"
Output: False
"""


def str_in_str(str1, str2):
    str2_idx = 0
    ans = False

    for j in range(0, len(str1)):
        if str1[j] == str2[str2_idx]:
            str2_idx += 1
        else:
            str2_idx = 0
        if str2_idx == len(str2):
            ans = True
    return ans


a = "aaaaabaaaaabaaaaaa"
b = "aaaaaa"
print(f'a: {a}, b:{b}, Is str2 in str1? -> {str_in_str(a, b)}')

a = 'abababababac'
b = 'abc'
print(f'a: {a}, b:{b}, Is str2 in str1? -> {str_in_str(a, b)}')


# ----------------------------------------------------------------
#
# question 2
#
# ----------------------------------------------------------------
class A:
    a = 'a'
    _a = '_a'
    __a = '__a'  # 'private method'(though there is no 'private member in python'), thus you can NOT get this attribute unless you initialize this class and use methods inside this class. If you try to do so, for example, to get a private attribute through B(which inherits from A, but B does not initialize A), you will get an ERROR

    def __init__(self):
        self.init_a = 'init_a'

    def foo(self):
        return True


class B(A):
    """note.
    Although class B inherits from class A, B does not initialize,
    -> A does not initialize
    Thus, if you write: B()._foo() to return self.init_a, since B does not initialize A, and A does not initialize,
    there is no way to get an 'uninitialized object' from A, you will get an ERROR
    """
    def __init__(self):  # check the doc string above
        pass

    def foo(self):
        return False

    def _foo(self):
        return self.init_a


print(f'A.a: {A.a}')
# print(A.__a)  # FIXME: AttributeError: type object 'A' has no attribute '__a'
# print(A().__a)  # FIXME: AttributeError: 'A' object has no attribute '__a'
print(f'A().foo(): {A().foo()}')
print(f'B().a: {B().a}')
print(f'B().foo(): {B().foo()}')
# print(f'B()._foo(): {B()._foo()}')  # FIXME: AttributeError: 'B' object has no attribute 'init_a'


# ----------------------------------------------------------------
# TODO: follow up: how to get a 'private member' in python?
# ----------------------------------------------------------------
# FIXME: this will NOT work
class A:
    a = 'a'
    _a = '_a'
    __a = '__a'  # private method, thus you can get this attribute inside this class A

    def __init__(self):
        self.init_a = 'init_a'
        self.__a = '__a'  # private method, thus you can get this attribute inside this class A


# print(f'A().__a: {A().__a}')  # FIXME: this will NOT work -> AttributeError: 'A' object has no attribute '__a'


# [In Python, actually, there is no such thing declared or anything that can be called a private member](https://www.educba.com/python-private-variables/)
# [How to access private variable outside the class in Python](https://tutorial.eyehunts.com/python/how-to-access-private-variable-outside-the-class-in-python-example-code/)
# TODO: ACCESS THROUGH METHOD -> CHECK this: 'Outside the class, you can’t access the private variable, but inside the class, you can access the private variables.'
class myClass:
    __amount = 15

    def hello(self):
        print("Amount is ", myClass.__amount)  # when you get a 'private member' inside this class by using this class' method, it works


# myClass.__amount  # AttributeError: type object 'myClass' has no attribute '__amount'
# myClass.hello()  # FIXME: TypeError: hello() missing 1 required positional argument: 'self'
myClass().hello()


class myClass_2:
    __amount = 25

    @staticmethod
    def hello():  # define a method to access that 'private member'
        print("Amount is ", myClass_2.__amount)  # when you get a 'private member' inside this class by using this class' method, it works


myClass_2.hello()


# ----------------------------------------------------------------
# TODO: follow up:  myClass v.s. myClass() -> what's the difference?
# ----------------------------------------------------------------
# google: python class with and without parentheses different
# [Instancing a class - difference between with and without brackets](https://stackoverflow.com/questions/28309757/instancing-a-class-difference-between-with-and-without-brackets)
a = myClass  # a and myClass identical at this point.  The interpreter won't care which you use.
print(f'a: {a}')
a_instance = myClass()  # instance of myClass
print(f'a_instance: {a_instance}')
"""
>>> a = myClass
>>> a
<class __main__.myClass at 0x10cd1de20>
>>> b = myClass()
>>> b
<__main__.myClass instance at 0x10cd8efc8>
"""


# ----------------------------------------------------------------
#
# question 3: the code below are correct, but how do you improve it?
# hint: there are redundant code -> object-oriented -> 'do not repeat yourself'
#
# ----------------------------------------------------------------
class A:
    mood = "Maintaining a good mood."
    Str = ''
    Int = 0
    List = []  # list()
    Dict = {}
    Tuple = ()
    Set = set()


class B:
    mood = "Keep up the good mood."
    Str = ""
    Int = 0
    List = []
    Dict = {}
    Tuple = ()
    Set = set()


class C:
    mood = "Happy every day."
    Str = ""
    Int = 0
    List = []
    Dict = {}
    Tuple = ()
    Set = set()


print(A.Str)
print(B.Int)
print(C.List)

# ----------------------------------------------------------------
# answer 3 - method 1: inherit
# ----------------------------------------------------------------
class A:
    mood = "Maintaining a good mood."
    Str = ''
    Int = 0
    List = []  # list()
    Dict = {}
    Tuple = ()
    Set = set()


class B(A):
    mood = "Keep up the good mood."


class C(A):
    mood = "Happy every day."


# ----------------------------------------------------------------
# answer 3 - method 2: inherit from a base class
# ----------------------------------------------------------------
class Base:
    # TODO -> compare self.Str in __init__ v.s. statics attr: use __init__(self) -> we do initialize the object -> slow
    def __init__(self):
        # List = []  # 變化
        self.Str = ''
    Str = ''  # TODO -> compare it with the mentioned above: statics attr, we do not initialize it -> fast

    Int = 0
    List = []  # list()
    Dict = {}
    Tuple = ()
    Set = set()


# ----------------------------------------------------------------
# TODO: follow up: Difference between list() and creating a list through []
# ----------------------------------------------------------------
"""my conclusion
1. about the 'speed' to create a list
2. about the 'elements'
[] just wraps the entire item in square brackets [], making it a one-item list
However, list() iterates over the dictionary (getting keys) and produces a list out of them

--
a = list()
b = []
-> they both create an empty list, but creating by [] is faster and list() is slower

[Why is [] faster than list()?](https://stackoverflow.com/questions/30216000/why-is-faster-than-list)
Because [] and {} are literal syntax. Python can create bytecode just to create the list or dictionary objects
list() and dict() are separate objects. Their names need to be resolved, the stack has to be involved to push the arguments, the frame has to be stored to retrieve later, and a call has to be made. That all takes more time.

--
(https://stackoverflow.com/questions/23025975/getting-past-slow-list-creation-in-python)
"""

# [difference between creating a new object of class 'list' and creating an object of other user defined class](https://stackoverflow.com/questions/67576083/difference-between-creating-a-new-object-of-class-list-and-creating-an-object)
"""
my_list = [1, 2, 3] works because the Python interpreter treats this syntax in a special way: 
[1, 2, 3] means "create a list object populated with these values".


list is a class, and calling list() is literally calling the class constructor. If you want, you can pass an iterable as an argument, and it will build the list from the elements of that iterable.
However, python allows "list literals" (along with tuple literals, set literals, and dict literals), which allow you to create a pre-built list with a certain set of elements. This is the same as with numbers and strings, which you can also give as literals instead of using their constructors:

print(str())  # empty string
print(int())  # 0
"""
mylist = list()
print(f'type(mylist): {type(mylist)}')  # <class 'list'>
mylist_2 = []
print(f'type(mylist_2): {type(mylist_2)}')  # <class 'list'>


# [Difference between using [] and list() in Python](https://stackoverflow.com/questions/23703109/difference-between-using-and-list-in-python)
"""
# The former just wraps the entire item in square brackets [], making it a one-item list:
>>> [{'foo': 1, 'bar': 2}]
[{'foo': 1, 'bar': 2}]

>>> obj = {1: 2, 3: 4, 5: 6, 7: 8}
>>> [obj]
[{1: 2, 3: 4, 5: 6, 7: 8}]

-

# The latter iterates over the dictionary (getting keys) and produces a list out of them:
>>> list({'foo': 1, 'bar': 2})
['foo', 'bar']

>>> obj = {1: 2, 3: 4, 5: 6, 7: 8}
>>> list(obj)
[1, 3, 5, 7]

This is because, when you loop over with a for loop, it only takes the keys as well:
>>> for k in obj:
...     print k
... 
1
3
5
7


But if you want to get the keys and the values, use .items():
>>> list(obj.items())
[(1, 2), (3, 4), (5, 6), (7, 8)]

Using a for loop:
>>> for k, v in obj.items():
...     print k, v
... 
1 2
3 4
5 6
7 8

"""

# [Difference between list() and creating a list through []](https://stackoverflow.com/questions/66164110/difference-between-list-and-creating-a-list-through)
"""
# list('123') iterates over each character of the string, turning an empty string into an empty list
>>> list('123')
['1', '2', '3']

# ['123'] creates a list containing a single, empty string.
>>> ['123']
['123']
"""


# [Difference between list() vs. [] when turning a set into a list [duplicate]](https://stackoverflow.com/questions/43197277/difference-between-list-vs-when-turning-a-set-into-a-list)
"""
Regarding the set conversion list(set(...)) this does create a new list but the members are taken by iterating through the set.

>>> set('test')
set(['s', 'e', 't']) # a test set
>>> list(set('test'))
['s', 'e', 't'] # create a list with members from set
>>> [set('test')]
[set(['s', 'e', 't'])] # create a list with a single member (which is the test set itself)
"""


# ----------------------------------------------------------------
#
# question 4
#
# ----------------------------------------------------------------

# Input:
matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

# Output: [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]]

# Input:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
length = len(matrix[0])
new_matrix = list()
for idx in range(0, length):
    new_lst = list()
    for i in range(0, len(matrix))[::-1]:  # for i in range(len(matrix), -1, -1) is faster, because it does not do further step to 'reverse'
        print(f'i: {i}')
        new_lst.append(matrix[i][idx])
    new_matrix.append(new_lst)
print(f'new_matrix: {new_matrix}')


# ----------------------------------------------------------------
#
# question 5
#
# ----------------------------------------------------------------
"""
承上題反轉矩陣，請原地修改值，不要分配額外的一維矩陣或二維陣列。
i.e., do NOT allocate new memory spaces, use the in-place replacement method
"""

"""my notes when figuring it out.
m20 -> m00
m10 -> m10
m00 -> m02

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]



sol.
step1. use for/while loop to swap 'row_idx' with 'col_idx' (along with the diagonal ??)
    so the 'current_matrix' can be:
    [[1, 4, 7],
     [2, 5, 8],
     [3, 6, 9]]

step2. 'reverse' for each list
    so the 'current_matrix' can be:
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
"""


# ----------------------------------------------------------------
#
# question 6: instance
# hint: 'memory address 記憶體位置' & .isinstance()
#
# ----------------------------------------------------------------
print(f'0 == False: {0 == False}')  # a more obscure method to tell differences -> True, because they both mean the similar concept to 'None'
print(f'0 is False: {0 is False}')  # a more precise method, it examines 'memory address' -> False, because their 'memory address' are different


def get():
    return True, False  # it returns a tuple because there are two elements


def get_2():
    return True,  # it returns a boolean because there is only one element


print(f'get(): {get()}, type(get()): {type(get())}')
print(f'get_2(): {get_2()}, type(get_2()): {type(get_2())}')
