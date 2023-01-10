#  ---  LIST  ----------------------------------------------------------------
print('---  LIST -----------------------------------------------------------')

x = [4, True, 'hi']
print(len(x))  # 3

y = 'hi'
print(len(y))  #2

x.append('hello')  # append does -> add to the end (only one element)
print(x)

x.extend([1, 10, 100])  # extend does -> append elements to the specific list
print(x)

x.pop()  # removes the last element
print(x)
x.pop(0)  # removes the element at the indicated position (arg: index)
print(x)

# the list data type and its cousin(primo), the tuple.
# https://automatetheboringstuff.com/2e/chapter4/#calibre_link-713
tupla = (30, 60, 90, 'bye', False)
print(tupla)


#  ---  FOR LOOPS  ----------------------------------------------------------------------
print('---  FOR LOOPS ----------------------------------------------------------------')

for i in range(5):  # range(start, stop, step)
  print(i)

print('----------------------------')

x = [2, 4, 6, 8, 10]
for i in range(len(x)):
  print(x[i])

print('----------------------------')

a = ('apple', 'banana', 'cherry')
b = enumerate(a)
print(list(b))
for index, element in enumerate(x):  # I use enumerate() because I need to use the index
  print(index, element)


#  ---  WHILE  ----------------------------------------------------------------------
print('---  WHILE  ----------------------------------------------------------------')
i = 1
while i < 6:
  print(i)
  i += 1  # i = i + 1

print('----------------------------')
j = 1
while j < 6:
  print(j)
  if (j == 3):
    break
  j += 1

print('----------------------------')
i = 0
while i < 6:
  i += 1
  if i == 3:  # Note that number 3 is missing in the result
    continue
  print(i)

print('----------------------------')
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")


#  ---  The Slice Operator  --------------------------------------------------------------------
print('---  The Slice Operator  ---------------------------------------------------------------')
# TODO: https://runestone.academy/ns/books/published/fopp/Sequences/TheSliceOperator.html#:~:text=The%20slice%20operator%20%5Bn%3Am,and%20including%20the%20mth%20character.
# slice [start, stop, step]
fruit = "banana"
print(fruit[:3])  # ban
print(fruit[3:])  # ana

julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
print(julia[2]) # 1967
print(julia[2:6]) # (1967, 'Duplicity', 2009, 'Actress')


#  ---  Sets  --------------------------------------------------------------------
print('---  Sets  --------------------------------------------------------------')
mySet = {11, 22, 33}
print(mySet)   # {33, 11, 22}  The set list is unordered, meaning: the items will appear in a random order.

mySet = {11, 22, 33, 33, 22}
print(mySet)   # {33, 11, 22}  Sets cannot have two items with the same value.
print(len(mySet))   # 3

myset = {"apple", "banana", "cherry"}
print(type(myset))

# The set() Constructor
thisset = set(("apple", "banana", "cherry"))   # It is also possible to use the set() constructor to make a set.
print(thisset)


#  ---  Dictionaries  --------------------------------------------------------------------
print('---  Dictionaries  --------------------------------------------------------------')
x = {'player': 'CR7'}
x['number'] = 7       # Inject data into our dictionary
print(x)
x['captain'] = True   # Inject data into our dictionary
print(x)

print('player' in x)      # True
print(x.values())         # dict_values(['CR7', 7, True])
print(x.keys())           # dict_keys(['player', 'number', 'captain'])
print(list(x.values()))   # ['CR7', 7, True]
print(list(x.keys()))     # ['player', 'number', 'captain']

del x['captain']
print(x)          # {'player': 'CR7', 'number': 7}

for key, value in x.items():
  print(key, value)     # player CR7  /n  number 7


#  ---  Comprehensions  --------------------------------------------------------------------
print('---  Comprehensions  --------------------------------------------------------------')
# https://ellibrodepython.com/list-comprehension-python
# sintax -> listname = [expresion for element in iterable]
# Comprehensions: Allow us to create list, dictionaries, tuples ... in one line of code.
squares = [i**2 for i in range(5)]      # expresion can be an operation, contant value, call to a function.
print(squares)     # [0, 1, 4, 9, 16]

# same code, but no using Comprehensions
squares = []
for i in range(5):
  squares.append(i**2)
print(squares)     # [0, 1, 4, 9, 16]


#  ---  Args & **Kwargs  --------------------------------------------------------------------
print('---  Args & **Kwargs  --------------------------------------------------------------')
#unpacking operator (*)
def my_sum(*args):
  result = 0
  # Iterating over the Python args tuple
  for x in args:
    result += x
  return result
print('my_sum:', my_sum(5, 5, 10))

def my_sum_2(**kwargs):
  result = 0
  for key, value in kwargs.items():
    print(key, "=", value)
    result += value
  return result
print('my_sum_2:', my_sum_2(a=10, b=10, c=20))

def concatenate(**kwargs):
  result = ""
  for arg in kwargs.values():
    result += arg
    # result += arg + " "
  return result
print('concatenate:', concatenate(a="Real", b="Python", c="is", d="great!"))

my_list = [1, 2, 3]
print(my_list)     # [1, 2, 3]
print(*my_list)    # 1 2 3


#  ---  Scope & Globals  --------------------------------------------------------------------
print('---  Scope & Globals  --------------------------------------------------------------')
x = 'Shingo'

def func(name):
  x = name

print(x)      # Shingo
func('Kim')
print(x)      # Shingo


#  ---  Exceptions  --------------------------------------------------------------------
print('---  Exceptions  --------------------------------------------------------------')
# Errors handler
# https://ellibrodepython.com/excepciones-try-except-finally
  # raise
  # Else, try, except, finally

#  ---  Handling Exceptions  --------------------------------------------------------------------
print('---  Handling Exceptions  --------------------------------------------------------------')
try:
  x = 7 / 0
except Exception as e:     # e is the variable when we will be store the exception=>error
  print(e)     # division by zero


#  ---  Lambda  --------------------------------------------------------------------
print('---  Lambda  --------------------------------------------------------------')
# Anonimous function, one line, any args
x = lambda x: x + 10

print(x(10))      # 20


#  ---  map & filter --------------------------------------------------------------------
print('---  map & filter  --------------------------------------------------------------')
x = [1, 2, 3, 4, 5]
mp = map(lambda i : i * 10, x) # map() must have at least two arguments.
print(list(mp))      # [10, 20, 30, 40, 50]

fil = filter(lambda i : i % 2 == 0, x) # filter need a boolean
print(list(fil))     # [2, 4]

def myfunc(a, b):
  return a + b
x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)      # <map object at 0x000001F871BFFAF0>
#convert the map into a list, for readability:
print(list(x))      # ['appleorange', 'bananalemon', 'cherrypineapple']


#  ---  F Strings --------------------------------------------------------------------
print('---  f strings  --------------------------------------------------------------')
# are new in python 3.6.







# import random
# for i in range(5):
#     print(random.randint(1, 10))
