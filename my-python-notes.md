# My Python Notes

# To-Do

- Write Data Structures similar to Java
- Iterate a string
- Pack & Unpack (\* & **) = jovian function(**test[input]) dictionary
- return type in a function? (LeetCode 34)
- super keyword in class inheritance
- isinstance keyword to check for appropriate data type
- empty set and other data structures (list) creation
- 1d & 2d array initialisation and delacre with 0 value set (https://www.youtube.com/live/bCPsBxEyQgc?si=lMallH2O9LYeuEv9&t=3927
  and
  https://www.youtube.com/live/SmOrBW22R2k?si=Y_9a5XTQX7_-fuWR&t=1003)
- swap values in python (list and simple variable)
- pass by value or reference
- same variable name for parameter & local variable. Which one gets updated on assignment?
- slice list [0:10] what if [11:10] or [-1:-2]
- Addition of two list and multiplication of string (‘ ’\*3) & list -**repr** vs **str** (Jovian Lec3 Assignment Section - https://www.youtube.com/live/M6NJUfT14aY?si=7Ep8590t9Cszo_xh&t=6260)
- pass function name as parameter to a method (custom merge sort Jovian Lec3- https://www.youtube.com/live/M6NJUfT14aY?si=mVOgNIr7y4tz3mSa&t=5460)
- multiple assignment in one line (a, b, c = 1, 2, 3) (int a = 1, b = 2, c = 3)
- function inside a function
- Optional to handle None case
- Time Constraint & Complexity Relationship: (https://www.youtube.com/shorts/6j8uLDZMXUg)
- list, tuple, dictionary iteration and stuff
- range, enumerate, while
- .join() str (https://www.youtube.com/live/SmOrBW22R2k?si=8d5kbhK7gRH8Hmyf&t=1570)
- [] \* 10 / range() for array initialize and declare (https://www.youtube.com/live/SmOrBW22R2k?si=Nsqup5G7dxLXvepE&t=2526)
- Zip with list (https://www.youtube.com/live/SmOrBW22R2k?si=5IGZON-VGNwEiJVa&t=5046)
- infinity in python (float(‘inf’))
- ternary operator
- power operator
- .format in print()
- OOP local variable & constructor initialize

# Vid-Reference

- Syntax Crash Course: https://www.youtube.com/watch?v=0K_eZGS5NsU
- DS Algo Course in Python: https://www.youtube.com/watch?v=pkYVOmU3MgA or
  https://www.youtube.com/watch?v=Jh4t9o2y_pw&list=PLyMom0n-MBrqFwguQhbCu0Anlxoel08dr or https://jovian.com/learn/data-structures-and-algorithms-in-python
- Syntax Course (by Bucky): https://youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_&si=37AiUm_pEOOA6_4b
- OOP in Python: https://www.youtube.com/watch?v=Ej_02ICOIgs and https://www.youtube.com/watch?v=qiSCMNBIP2g and https://www.youtube.com/watch?v=JeznW_7DlB0

# String

### split

```python
string = "Hello-World-!"
my_list = string.split("-")  # ['Hello', 'World', '!']
```

### slice / substring

```python
string = "Hello-World-!"
my_string = string[1:5] # "ello" {1 to 5}
```

### reverse

```python
string = "".join(reversed("hello"))  # "olleh"
```

### sort

```python
# Ascending Order
string = "".join(sorted("hello"))  # "ehllo"
# Descending Order
string = "".join(sorted("hello", reverse=True))  # "ollhe"
```

### upper & lower

```python
string = str.upper("hello") # "HELLO"
string = str.lower("WORLD") # "world"
```

### string character checks

```python
var = "abc"

print(var.isalnum())  # True
print(var.isalpha())  # True
print(var.isdigit())  # False
print(var.islower())  # True
print(var.isupper())  # False
```

### == VS is

```python
var1 = "hello world"
var2 = " ".join(["hello", "world"])

print(var1 == var2)  # True (Cuz Value Comparison)
print(var1 is var2)  # Flase (Cuz Object Comparison)
```

# List

### initialization

```python
# Declare
my_list = []
my_list = list()

# Declare and Initialize
my_list = ["var1", 2, "var 3"]
my_list = list(["var1", 2, "var 3"])
```

### iterate

```python
my_list = ["var1", 2, "var 3"]

# Using range
for index in range(0, len(my_list)): # 0 to len(my_list)-1
   print(index, my_list[index])

# Using enumerate
for index, element in enumerate(my_list):
   print(index, element)

# Using for-each loop
for element in my_list:
   print(element)
```

### slice / sub-list

```python
my_list = ["var1", 2, "var 3"]
new_list = my_list[1:3] # [2, 'var 3'] (index 1 to index 2)
```

### copy

```python
my_list = [[[3]], -7, 1, 5, 2, -2]

# Top Layer Copy
new_list = my_list[:]
new_list = list(my_list)
new_list = my_list.copy()
new_list = [x for x in my_list]
# new_list[0][0][0] = 100
# my_list = [[[100]], -7, 1, 5, 2, -2]
# new_list = [[[100]], -7, 1, 5, 2, -2]

# Deep Copy
import copy
new_list = copy.deepcopy(my_list)
# new_list[0][0][0] = 100
# my_list = [[[3]], -7, 1, 5, 2, -2]
# new_list = [[[100]], -7, 1, 5, 2, -2]
```

### size

```python
length = len(my_list)
```

### add

```python
# Add at the end
my_list.append("element")

# Add at an index
index = 2
my_list.insert(index, "element")

# Add at the end by +=
my_list += ["element"]
```

### update

```python
index = 2
my_list[index] = "element"
```

### remove

```python
index = 2
my_list.pop(index)
```

### contains

```python
flag = "d" in my_list  # False
flag = "d" not in my_list  # True
```

### get

```python
my_list = ["a", "b", "c", "d"]

my_list[0] # a = First element
my_list[2] # c = Element at index 2
my_list[-1] # d = Last element

my_list[4]  # IndexError: Allowed = 0, 1, 2, 3
my_list[-5] # IndexError: Allowed = -4, -3, -2, -1
```

### sum

```python
my_list = [1, 2, 3, 4]
sum(my_list) # 10
```

### sort

```python
my_list = [3, -7, 1, 5, 2, -2]

# InPlace Vanilla Sort
my_list.sort()
my_list.sort(reverse=True)

# OutOfPlace Vanilla Sort
new_list = sorted(my_list)
new_list = sorted(my_list, reverse=True)

# Using key InPlace Sort
my_list.sort(key=abs)
my_list.sort(key=abs, reverse=True)

# Using key OutOfPlace Sort
new_list = sorted(my_list, key=abs)
new_list = sorted(my_list, key=abs, reverse=True)

# Using lambda InPlace Sort
my_list.sort(key=lambda x: (-abs(x), x))

# Using lambda OutOfPlace Sort
new_list = sorted(my_list, key=lambda x: (-abs(x), x))



def sort_by_abs_then_normal(item):
   return (-abs(item), item)


# Using key = custom function InPlace Sort
my_list.sort(key=sort_by_abs_then_normal)

# Using key = custom function OutOfPlace Sort
new_list = sorted(my_list, key=sort_by_abs_then_normal)
```

### sort (class)

```python
class MyClass:
   def __init__(self, string: str = "") -> None:
       self.string = string

   def __repr__(self):  # Backup if __str__ is not defined
       return self.string

   def __str__(self):
       self.__repr__()


myclass_list = [MyClass("abc"), MyClass("def"), MyClass(), MyClass("python")]

# Using lambda InPlace Sort
myclass_list.sort(key=lambda x: (-len(x.string), x.string))

# Using lambda OutOfPlace Sort
new_myclass_list = sorted(myclass_list, key=lambda x: (-len(x.string), x.string))


def sort_by_len_then_normal(item):
   return (-len(item.string), item.string)


# Using key = custom function InPlace Sort
myclass_list.sort(key=sort_by_len_then_normal)

# Using key = custom function OutOfPlace Sort
new_myclass_list = sorted(myclass_list, key=sort_by_len_then_normal)
```

# Tuple

### initialization

```python
# Declare
my_tuple = ()
my_tuple = tuple()

# Declare and Initialize
my_tuple = "var1", 2, "var 3"
my_tuple = ("var1", 2, "var 3")
my_tuple = tuple(["var1", 2, "var 3"])
```

### iterate

```python
my_tuple = ("var1", 2, "var 3")

# Using range
for index in range(0, len(my_tuple)):  # 0 to len(my_tuple)-1
   print(index, my_tuple[index])

# Using enumerate
for index, element in enumerate(my_tuple):
   print(index, element)

# Using for-each loop
for element in my_tuple:
   print(element)
```

### slice / sub-tuple

```python
my_tuple = ("var1", 2, "var 3")
new_tuple = my_tuple[1:3]  # (2, 'var 3') (index 1 to index 2)
```

### copy

```python
my_tuple = ([[3]], -7, 1, 5, 2, -2)

# Top Layer Copy
new_tuple = my_tuple[:]
new_tuple = tuple(my_tuple)
new_tuple = my_tuple
# new_tuple[0][0][0] = 100
# my_tuple = ([[100]], -7, 1, 5, 2, -2)
# new_tuple = ([[100]], -7, 1, 5, 2, -2)

# Deep Copy
import copy
new_tuple = copy.deepcopy(my_tuple)
# new_tuple[0][0][0] = 100
# my_tuple = [[[3]], -7, 1, 5, 2, -2]
# new_tuple = [[[100]], -7, 1, 5, 2, -2]
```

### size

```python
length = len(my_tuple)
```

### add

```python
# NOT POSSIBLE as tuple is immutable
```

### update

```python
# NOT POSSIBLE as tuple is immutable
```

### remove

```python
# NOT POSSIBLE as tuple is immutable
```

### contains

```python
flag = "d" in my_tuple  # False
flag = "d" not in my_tuple  # True
```

### get

```python
my_tuple = ("a", "b", "c", "d")

my_tuple[0]  # a = First element
my_tuple[2]  # c = Element at index 2
my_tuple[-1]  # d = Last element

my_tuple[4]  # IndexError: Allowed = 0, 1, 2, 3
my_tuple[-5]  # IndexError: Allowed = -4, -3, -2, -1
```

### sum

```python
my_tuple = (1, 2, 3, 4)
sum(my_tuple)  # 10
```

### sort

```python
my_tuple = (3, -7, 1, 5, 2, -2)

# InPlace Vanilla Sort
# NOT POSSIBLE as tuple is immutable

# OutOfPlace Vanilla Sort
new_tuple = tuple(sorted(my_tuple))
new_tuple = tuple(sorted(my_tuple, reverse=True))

# Using key InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using key OutOfPlace Sort
new_tuple = tuple(sorted(my_tuple, key=abs))
new_tuple = tuple(sorted(my_tuple, key=abs, reverse=True))

# Using lambda InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using lambda OutOfPlace Sort
new_tuple = tuple(sorted(my_tuple, key=lambda x: (-abs(x), x)))


def sort_by_abs_then_normal(item):
   return (-abs(item), item)


# Using key = custom function InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using key = custom function OutOfPlace Sort
new_tuple = tuple(sorted(my_tuple, key=sort_by_abs_then_normal))
```

### sort (class)

```python
class MyClass:
   def __init__(self, string: str = "") -> None:
       self.string = string

   def __repr__(self):  # Backup if __str__ is not defined
       return self.string

   def __str__(self):
       self.__repr__()


myclass_tuple = (MyClass("abc"), MyClass("def"), MyClass(), MyClass("python"))

# Using lambda InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using lambda OutOfPlace Sort
new_myclass_tuple = tuple(
   sorted(myclass_tuple, key=lambda x: (-len(x.string), x.string))
)


def sort_by_len_then_normal(item):
   return (-len(item.string), item.string)


# Using key = custom function InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using key = custom function OutOfPlace Sort
new_myclass_tuple = tuple(sorted(myclass_tuple, key=sort_by_len_then_normal))
```

# Set

### initialization

```python
# Declare
# my_dict = {} (Creates a dict NOT a set)
my_set = set()

# Declare and Initialize
my_set = {"var1", 2, "var 3"}
my_set = set(["var1", 2, "var 3"])

# NOT POSSIBLE to create set that keeps element sorted
# NOT POSSIBLE to create set that maintains insertion order
```

### iterate

```python
my_set = set(["var1", 2, "var 3"])

# Using range
# NOT POSSIBLE as set is unordered or unindexed

# Using enumerate
for index, element in enumerate(my_set):
   print(index, element)

# Using for-each loop
for element in my_set:
   print(element)
```

### slice / sub-set

```python
# NOT POSSIBLE as set is unordered or unindexed
```

### copy

```python
my_set = {((3, 4)), -7, 1, 5, 2, -2}
# Can't create set with mutable elements (e.g list) Hence layer copy doesn't matter for set

# Top Layer Copy
new_set = set(my_set)
new_set = my_set.copy()
new_set = {x for x in my_set}

# Deep Copy
import copy
new_set = copy.deepcopy(my_set)
```

### size

```python
length = len(my_set)
```

### add

```python
my_set = {1, 2, 3}

# Add single element
my_set.add("Hello")

# Add multiple elements
my_set.update("world", [4], {9}, (12, 13), {"key": 10, 8: 10})
# Elements can be string, list, set, tuple and dict
# Only keys get added in set as only keys of dict are unique

# Add multiple elements and generate a new set
new_set = my_set.union({5, 6})
```

### remove

```python
my_set = {(3, 4), -7, 1, 5, 2, -2}

# Remove element and NOT throw error if element doesn't exist
my_set.discard((3, 4))

# Remove ALL the elements
my_set.clear()
```

### contains

```python
flag = "d" in my_set  # False
flag = "d" not in my_set  # True
```

### get

```python
# NOT POSSIBLE to get or access elements by index as set is an unordered collection of unique elements
```

### sum

```python
my_set = {1, 2, 3, 4}
sum(my_set)  # 10
```

### sort

```python
# NOT POSSIBLE as set is unordered.
# Convert into list and then sort.

# FYI: Can't create set that stores element in sorted order or maintains the insertion order.
```

### sort (class)

```python
# NOT POSSIBLE as set is unordered.
# Convert into list and then sort.

# FYI: Can't create set that stores element in sorted order or maintains the insertion order.
```

# Dictionary

```python
print("STILL EDITING THIS SECTION")
```

# Conversions

### 1. String & List

```python
new_list = list("var 3")  # ['v', 'a', 'r', ' ', '3']

my_string = "".join(["v", "a", "r", " ", "3"])  # "var 3"
```

### 2. Dictionary & List

```python
new_dict = dict(zip(["var1", "var2", "var3"], [1, 2, 3]))

# [('var1', 1), ('var2', 2), ('var3', 3)]
items = list(new_dict.items())

# ['var1', 'var2', 'var3']
keys = list(new_dict.keys())

# [1, 2, 3]
values = list(new_dict.values())
```

### 3. Tuple & List

```python
new_tuple = tuple(["var1", 2, "var 3"])

new_list = list(("var1", 2, "var 3"))
```

### 4. Set & List

```python
new_set = set(["var1", 2, "var 3"])

new_list = list({"var1", 2, "var 3"})
```

# MyClass

### init, repr, str, eq, hash

```python
class MyClass:
   def __init__(self):
       self.v1 = None
       self.v2 = None

   def __repr__(self): # Backup if __str__ is not defined
       return "({}, {})".format(self.v1, self.v2)

   def __str__(self):
       self.__repr__()

   def __eq__(self, other):
       return self.v1 == other.v1 and self.v2 == other.v2

   def __hash__(self):
       return hash((self.v1, self.v2))
```

# Python Syntax

### print

```python
print("Hello", "World", sep="-")  # Hello-World
print("Hello", "World", end="!\n")  # Hello World!
print("Hello", "World", sep="-", end="!\n")  # Hello-World!
```

### lambda

#### filter

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6, 8, 10]
```

#### map

```python
nums = [1, 2, 3, 4, 5]
list(map(lambda x: x ** 2, nums)) # [1, 4, 9, 16, 25]
```
