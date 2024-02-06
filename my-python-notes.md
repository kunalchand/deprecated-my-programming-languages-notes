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
- | operator in python
- Counter() dict + sort coutner dict

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
for index in range(0, len(my_list), 1): # 0 to len(my_list)-1
   print(index, my_list[index])

# Using for-each loop
for element in my_list:
   print(element)

# Using enumerate
for index, element in enumerate(my_list):
   print(index, element)
```

### slice / sub-list

```python
my_list = ["var1", 2, "var 3"]
new_list = my_list[1:3] # [2, 'var 3'] (index 1 to index 2)
```

### copy

```python
my_list = [[[3]], -7, 1, 5, 2, -2]

# Top Layer Copy (Shallow Copy)
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
# Update value at the given index
index = 2
my_list[index] = "element"
```

### remove

```python
index = 2
my_list.pop(index)
```

### clear

```python
# Remove ALL element from list
my_list.clear()
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


def custom_function(item):
    return (-abs(item), item)


# Using key = custom function InPlace Sort
my_list.sort(key=custom_function)

# Using key = custom function OutOfPlace Sort
new_list = sorted(my_list, key=custom_function)


def custom_method(a, b):
    if abs(a) > abs(b):
        return -1 # a comes BEFORE b
    elif abs(a) < abs(b):
        return 1 # a comes AFTER b
    else:
        if a > b:
            return 1 # a comes AFTER b
        elif a < b:
            return -1 # a comes BEFORE b
        else:
            return 0


# Using key = cmp_to_key InPlace Sort
from functools import cmp_to_key
my_list.sort(key=cmp_to_key(custom_method))

# Using key = cmp_to_key OutOfPlace Sort
from functools import cmp_to_key
new_list = sorted(my_list, key=cmp_to_key(custom_method))
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


my_list = [MyClass("abc"), MyClass("def"), MyClass(), MyClass("python")]

# Using lambda InPlace Sort
my_list.sort(key=lambda x: (-len(x.string), x.string))

# Using lambda OutOfPlace Sort
new_list = sorted(my_list, key=lambda x: (-len(x.string), x.string))


def custom_function(item):
    return (-len(item.string), item.string)


# Using key = custom function InPlace Sort
my_list.sort(key=custom_function)

# Using key = custom function OutOfPlace Sort
new_list = sorted(my_list, key=custom_function)


def custom_method(a, b):
    if len(a.string) == 0 and len(b.string) != 0:
        return -1  # a comes BEFORE b
    elif len(a.string) != 0 and len(b.string) == 0:
        return 1  # a comes AFTER b
    else:
        # Both strings have a length greater than 0, compare the strings
        if a.string > b.string:
            return -1  # a comes BEFORE b
        elif a.string < b.string:
            return 1  # a comes AFTER b
        else:
            return 0  # a and b are equal


# Using key = cmp_to_key InPlace Sort
from functools import cmp_to_key
my_list.sort(key=cmp_to_key(custom_method))

# Using key = cmp_to_key OutOfPlace Sort
from functools import cmp_to_key
new_list = sorted(my_list, key=cmp_to_key(custom_method))
```

# Tuple

- Tuple has immutable elements
- Tuple can have mutable inner-elements.

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
for index in range(0, len(my_tuple), 1):  # 0 to len(my_tuple)-1
   print(index, my_tuple[index])

# Using for-each loop
for element in my_tuple:
   print(element)

# Using enumerate
for index, element in enumerate(my_tuple):
   print(index, element)
```

### slice / sub-tuple

```python
my_tuple = ("var1", 2, "var 3")
new_tuple = my_tuple[1:3]  # (2, 'var 3') (index 1 to index 2)
```

### copy

```python
my_tuple = ([[3]], -7, 1, 5, 2, -2)

# Top Layer Copy (Shallow Copy)
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

### clear

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


def custom_function(item):
    return (-abs(item), item)


# Using key = custom function InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using key = custom function OutOfPlace Sort
new_tuple = tuple(sorted(my_tuple, key=custom_function))


def custom_method(a, b):
    if abs(a) > abs(b):
        return -1
    elif abs(a) < abs(b):
        return 1
    else:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0


# Using key = cmp_to_key InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using key = cmp_to_key OutOfPlace Sort
from functools import cmp_to_key

new_tuple = tuple(sorted(my_tuple, key=cmp_to_key(custom_method)))
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


my_tuple = (MyClass("abc"), MyClass("def"), MyClass(), MyClass("python"))

# Using lambda InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using lambda OutOfPlace Sort
new_tuple = tuple(sorted(my_tuple, key=lambda x: (-len(x.string), x.string)))


def custom_function(item):
    return (-len(item.string), item.string)


# Using key = custom function InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using key = custom function OutOfPlace Sort
new_tuple = tuple(sorted(my_tuple, key=custom_function))


def custom_method(a, b):
    if len(a.string) == 0 and len(b.string) != 0:
        return -1  # a comes BEFORE b
    elif len(a.string) != 0 and len(b.string) == 0:
        return 1  # a comes AFTER b
    else:
        # Both strings have a length greater than 0, compare the strings
        if a.string > b.string:
            return -1  # a comes BEFORE b
        elif a.string < b.string:
            return 1  # a comes AFTER b
        else:
            return 0  # a and b are equal


# Using key = cmp_to_key InPlace Sort
# NOT POSSIBLE as tuple is immutable

# Using key = cmp_to_key OutOfPlace Sort
from functools import cmp_to_key

new_tuple = tuple(sorted(my_tuple, key=cmp_to_key(custom_method)))
```

# Set

- Set can only have immutable elements or inner-elements (e.g list) (Reference to element can't be changed. Basically element can be Class but not list).
- Set is unordered or unindexed.
- Can't create set that stores element in sorted order or maintains the insertion order.
- Order of element in set is random

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

# Using for-each loop
for element in my_set:
   print(element) # Order of elements is random

# Using enumerate
# Since set is unordered, generating index doesn't make sense
```

### slice / sub-set

```python
# NOT POSSIBLE as set is unordered or unindexed
```

### copy

```python
my_set = {((3, 4)), -7, 1, 5, 2, -2}
# Can't create set with mutable elements (e.g list) Hence layer copy doesn't matter for set

# Top Layer Copy (Shallow Copy)
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

### update

```python
# NOT POSSIBLE for set as set can't have mutable elements
```

### remove

```python
my_set = {(3, 4), -7, 1, 5, 2, -2}

# Remove element but NOT throw error if element doesn't exist
my_set.discard((3, 4))

# Remove element but THROW error if element doesn't exist
my_set.remove((7, "ab8", 9))

# Remove ALL the elements
my_set.clear()
```

### clear

```python
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
# NOT POSSIBLE as set is unordered. Gives random order in each iteration.
# Convert into list, then sort the list and then use sorted list.

# FYI: Can't create set that stores element in sorted order or maintains the insertion order.

my_set = {3, -7, 1, 5, 2, -2}

my_list = list(my_set)
# my_list = [1, 2, 3, 5, -7, -2]

new_list = sorted(my_list, key=lambda element: abs(element), reverse=True)
# new_list = [-7, 5, 3, 2, -2, 1]
```

### sort (class)

```python
# NOT POSSIBLE as set is unordered. Gives random order in each iteration.
# Convert into list, then sort the list and then use sorted list.

# FYI: Can't create set that stores element in sorted order or maintains the insertion order.

class MyClass:
    def __init__(self, string: str = "") -> None:
        self.string = string

    def __repr__(self):  # Backup if __str__ is not defined
        return self.string

    def __str__(self):
        self.__repr__()


my_set = {MyClass("abc"), MyClass("def"), MyClass(), MyClass("python")}

my_list = list(my_set)
# my_list = [def, , python, abc]

new_list = sorted(my_list, key=lambda x: len(x.string), reverse=True)
# new_list = [python, def, abc, ]
```

# Dictionary

- Dict has immutable elements or inner-elements (e.g list) as key (Reference to element can't be changed. Basically element can be class but not list).
- Dict can have mutalble value.
- Dict is unindexed.
- Can't create dict that keeps elements in sorted order wrt key or value.
- By DEFAULT in python, dictionary maintains insertion order of elements (both dict and defaultdict).

### initialization

```python
# Declare
my_dict = {}  # (Creates a dict NOT a set)
my_dict = dict()

# Declare and Initialize
my_dict = {"key1": "value1", "key2": "value2"}
my_dict = dict([("key1", "value1"), ("key2", "value2")])
my_dict = dict(
    zip(["key1", "key2"], ["value1", "value2"])
)  # Both lists should have same number of elements otherwise few pairs will go missing

from itertools import zip_longest

my_dict = dict(
    zip_longest(["key1", "key2", "key3"], ["value1", "value2"], fillvalue="missing")
)  # Fill the missing values with fillvalue

from collections import defaultdict

my_dict = defaultdict(
    list
)  # Default value is empty list so no need to create a new list for each new key, directly append
my_dict["key2"].append("value2")
my_dict["key1"].append("value1")

# NOT POSSIBLE to create dict that keeps elements in sorted order wrt key or value

# By DEFAULT in python, dictionary maintains insertion order of elements (both dict and defaultdict)
```

### slice / sub-dict

```python
# NOT POSSIBLE for dict
```

### copy

```python
my_dict = {("a", "b"): ["c", ["d"]], "e": 2}
# Can't create dict with mutable elements or inner-elements (e.g list) as key. Mutable values are allowed.

# Top Layer Copy (Shallow Copy)
new_dict = dict(my_dict)
new_dict = my_dict.copy()
new_dict = {k: v for k, v in my_dict.items()}
# new_dict[("a", "b")][1][0] = 5
# my_dict = {('a', 'b'): ['c', [5]], 'e': 2}
# new_dict = {('a', 'b'): ['c', [5]], 'e': 2}

# Deep Copy
import copy
new_dict = copy.deepcopy(my_dict)
# new_dict[("a", "b")][1][0] = 5
# my_dict = {('a', 'b'): ['c', ['d']], 'e': 2}
# new_dict = {('a', 'b'): ['c', [5]], 'e': 2}
```

### size

```python
length = len(my_dict)
```

### add

```python
my_dict = {"key1": 1, "key2": 2}

#  Insert a new key-value pair element in dict
my_dict["key"] = "value"
# FYI: It overrides value, if key already exists in dict (See Update)

# Concatinate two dicts
first_dict = {"key1": 1, "key2": 2}
second_dict = {"key3": 3, "key4": 4}
new_dict = {**first_dict, **second_dict}
new_dict = first_dict | second_dict
```

### update

```python
#  Override the existing key-value pair element and update its value in dict
my_dict["key"] = "new_value"
```

### remove

```python
my_dict = {"key1": "value1", "key2": "value2"}

# Removes the key-value pair element and returns the value if key exists or else THROWS KeyError
value = my_dict.pop("key")

# Removes the key-value pair element and returns the value if key exists or else returns default value (which can be set to None or any other value)
value = my_dict.pop("key", "default_value")

# Removes all key-value pair elements
my_dict.clear()
```

### clear

```python
# Removes all key-value pair elements
my_dict.clear()
```

### contains

```python
my_dict = {"key1": "value1", "key2": "value2"}

# Vanilla
key_flag = "key1" in my_dict  # O(1)

# Complex
key_flag = "key1" in my_dict.keys()  # O(1)
value_flag = "value1" in my_dict.values()  # O(n)
pair_flag = ("key1", "value1") in my_dict.items()  # O(n)
```

### get

```python
my_dict = {"key1": "value1", "key2": "value2"}

# Returns the value if key exists or else returns None
value = my_dict["key"]

# Returns the value if key exists or else returns None
value = my_dict.get("key")

# Returns the value if key exists or else returns default value (which can be set to None or any other value)
value = my_dict.get("key", "default_value")
```

### entry / item

#### iterate

```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Using for-each loop
for key, value in my_dict.items():
    print(key, value)

# Using enumerate
for index, (key, value) in enumerate(my_dict.items()):
    print(index, key, value)
```

### key

#### iterate

```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Vanilla for-each loop
for key in my_dict:
    value = my_dict[key]
    print(key, value)

# Using for-each loop
for key in my_dict.keys():
    value = my_dict[key]
    print(key, value)

# Using enumerate
for index, key in enumerate(my_dict.keys()):
    value = my_dict[key]
    print(index, key, value)
```

#### sum

```python
my_dict = {1: "value1", 2: "value2", 3: "value3"}

# Vanilla
sum(my_dict.keys())  # 6
```

#### sort

```python
# NOT POSSIBLE to create dict that keeps elements in sorted order wrt key
# Convert into list, then sort the list, then convert the sorted list into dict and then use dict.

# FYI: By DEFAULT in python, dictionary maintains insertion order of elements (both dict and defaultdict)

my_dict = {7: "value3", 8: "value1", 6: "value2"}

my_list = list(my_dict.items())
# my_list = [(7, 'value3'), (8, 'value1'), (6, 'value2')]

new_list = sorted(my_list, key=lambda entry: entry[0], reverse=True)
# new_list = [(8, 'value1'), (7, 'value3'), (6, 'value2')]

new_dict = dict(new_list)
# new_dict = {8: 'value1', 7: 'value3', 6: 'value2'}
```

#### sort (class)

```python
# NOT POSSIBLE to create dict that keeps elements in sorted order wrt key
# Convert into list, then sort the list, then convert the sorted list into dict and then use dict.

# FYI: By DEFAULT in python, dictionary maintains insertion order of elements (both dict and defaultdict)

class MyClass:
    def __init__(self, string: str = "") -> None:
        self.string = string

    def __repr__(self):  # Backup if __str__ is not defined
        return self.string

    def __str__(self):
        self.__repr__()


my_dict = {
    MyClass("abc"): 4,
    MyClass("def"): 3,
    MyClass(): 2,
    MyClass("python"): 1,
}

my_list = list(my_dict.items())
# my_list = [(abc, 4), (def, 3), (, 2), (python, 1)]

new_list = sorted(my_list, key=lambda entry: entry[0].string, reverse=True)
# new_list = [(python, 1), (def, 3), (abc, 4), (, 2)]

new_dict = dict(new_list)
# new_dict = {python: 1, def: 3, abc: 4, : 2}
```

### value

#### iterate

```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Using for-each loop
for value in my_dict.values():
    print(value)

# Using enumerate
for index, value in enumerate(my_dict.values()):
    print(index, value)
```

#### sum

```python
my_dict = {"key1": 1, "key2": 2, "key3": 3}

# Vanilla
sum(my_dict.values())  # 6
```

#### sort

```python
# NOT POSSIBLE to create dict that keeps elements in sorted order wrt value
# Convert into list, then sort the list, then convert the sorted list into dict and then use dict.

# FYI: By DEFAULT in python, dictionary maintains insertion order of elements (both dict and defaultdict)

my_dict = {7: "value3", 8: "value1", 6: "value2"}

my_list = list(my_dict.items())
# my_list = [(7, 'value3'), (8, 'value1'), (6, 'value2')]

new_list = sorted(my_list, key=lambda entry: entry[1], reverse=True)
# new_list = [(7, 'value3'), (6, 'value2'), (8, 'value1')]

new_dict = dict(new_list)
# new_dict = {7: 'value3', 6: 'value2', 8: 'value1'}
```

#### sort (class)

```python
# NOT POSSIBLE to create dict that keeps elements in sorted order wrt value
# Convert into list, then sort the list, then convert the sorted list into dict and then use dict.

# FYI: By DEFAULT in python, dictionary maintains insertion order of elements (both dict and defaultdict)

class MyClass:
    def __init__(self, string: str = "") -> None:
        self.string = string

    def __repr__(self):  # Backup if __str__ is not defined
        return self.string

    def __str__(self):
        self.__repr__()


my_dict = {
    4: MyClass("abc"),
    3: MyClass("def"),
    2: MyClass(),
    1: MyClass("python"),
}

my_list = list(my_dict.items())
# my_list = [(4, abc), (3, def), (2, ), (1, python)]

new_list = sorted(my_list, key=lambda entry: entry[1].string, reverse=True)
# new_list = [(1, python), (3, def), (4, abc), (2, )]

new_dict = dict(new_list)
# new_dict = {1: python, 3: def, 4: abc, 2: }
```

# Stack

- No built in data structure in python
- Using list as stack is efficient as add and remove are from the same end (right end of list)

### initialization

```python

# Delcare
stack = []

# Declare and Initialize
stack = [1, 2, 3]
```

### iterate

```python
stack = ["item1", "item2", "item3"]

# Vanilla Loop and Pop
while stack:
    item = stack.pop()
    print(item)

# Iterate over the stack from top to bottom (right end to left end of list)
for item in reversed(stack):
    print(item)
```

### size

```python
size = len(stack)
```

### add

```python
# Push (Insert at the right end of the list)
stack.append("apple")
```

### remove

```python
# Pop (Remove and return from the right end of the list)
element = stack.pop()
```

### clear

```python
# Remove ALL element from stack
stack.clear()
```

### contains

```python
flag = "d" in stack  # False
flag = "d" not in stack  # True
```

### peek

```python
stack = ["element1", "element2", "element3"]

# See the top item of stack (right end item of list) without removal
top_item = stack[-1] if stack else None # "element3"
```

# Queue

- Use deque as queue in python due to its efficient implementation
- Using list as queue is INefficient as add and remove are from the DIFFERENT end. (removing from start involves shifting all the elements hence O(n))

### initialization

```python
from collections import deque

# Declare
queue = deque()

# Declare and Initialize
queue = deque([1, 2, 3])
```

### iterate

```python
# Vanilla Loop and Pop
while queue:
    item = queue.popleft()
    print(item)

# Iterate like a list from left (queue exit) to right (queue entry)
for item in queue:
    print(item)
```

### size

```python
size = len(queue)
```

### add

```python
# Add to queue entry (list right end)
queue.append("item")
```

### remove

```python
# Remove from queue exit (list left end)
item = queue.popleft()
```

### clear

```python
# Remove ALL elements from deque (queue)
queue.clear()
```

### contains

```python
flag = "d" in queue  # False
flag = "d" not in queue  # True
```

### peek

```python
from collections import deque

queue = deque([1, 2, 3])

# See the item at queue exit (left end item of list) without removal
exit_item = queue[0] if queue else None # 1
```

# Deque

### initialisation

# Conversions

### 1. String & List

```python
new_list = list("var 3")
# new_list = ['v', 'a', 'r', ' ', '3']

new_string = "".join(["v", "a", "r", " ", "3"])
# new_string = "var 3"
```

### 2. Dictionary & List

```python
new_dict = dict([('var1', 1), ('var2', 2), ('var3', 3)])
# new_dict = {'var1': 1, 'var2': 2, 'var3': 3}

new_dict = dict(zip(["var1", "var2", "var3"], [1, 2, 3]))
# new_dict = {'var1': 1, 'var2': 2, 'var3': 3}

items = list(new_dict.items())
# items = [('var1', 1), ('var2', 2), ('var3', 3)]

keys = list(new_dict.keys())
# keys = ['var1', 'var2', 'var3']

values = list(new_dict.values())
# values = [1, 2, 3]
```

### 3. Tuple & List

```python
new_tuple = tuple(["var1", 2, "var 3"])
# new_tuple = ('var1', 2, 'var 3')

new_list = list(("var1", 2, "var 3"))
# new_list = ['var1', 2, 'var 3']
```

### 4. Set & List

```python
new_set = set(["var1", 2, "var 3"])
# new_set = {2, 'var 3', 'var1'}

new_list = list({"var1", 2, "var 3"})
# new_list = [2, 'var1', 'var 3']
```

# MyClass

### init, repr, str, eq, hash

- Defining **repr** is much safer that definding **str**
- **str** may or may not be directly called. But **repr** is either directly called or gets called when **str** is not present

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
