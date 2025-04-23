# Understanding Mutable and Immutable Objects in Python

## 1) Introduction

In Python, everything is an object, and each object has its own set of properties. Understanding how these objects work and how Python handles them is crucial for writing clean and efficient code. Specifically, understanding **mutable** and **immutable** objects can help you avoid unexpected bugs and optimize your program.

In this blog, we will explore what mutable and immutable objects are, how they behave in memory, and how this affects variable assignments, function arguments, and object references. We'll also go through examples to help solidify these concepts.

---

## 2) Id and Type

Every object in Python has two essential attributes: its **type** and its **identity**.

- **Type**: The type defines what kind of object the variable holds (such as `int`, `str`, `list`, etc.).
- **Identity**: The identity of an object refers to the memory address where the object is stored. This is unique to every object and can be checked using the `id()` function.

For example:

```python
a = [1, 2, 3]
print(id(a))  # Unique memory address of list a
print(type(a))  # <class 'list'>

If we modify a, its identity might change:

a = a + [4]
print(id(a))  # New memory address, since `+` creates a new list
```
However, in-place modifications like += will keep the object’s identity the same:
```python
a = [1, 2, 3]
a += [4]
print(id(a))  # Same memory address because the operation was in-place
```
The identity of objects is important when comparing objects in Python:
- **==** checks if two objects have the same value.

- **is** checks if two variables refer to the same object in memory.
````python
a = 100
b = 100
print(a == b)  # True: Same value
print(a is b)  # True: Same object (for small integers)

a = [1, 2]
b = [1, 2]
print(a == b)  # True: Same value
print(a is b)  # False: Different objects
````
## 3) Mutable Objects

Mutable objects are objects whose content can be changed after their creation without creating a new object. Common mutable objects include lists, dictionaries, and sets.

When modifying a mutable object, its identity remains the same. Let's see an example with lists:
````python
a = [1, 2, 3]
b = a  # b refers to the same object as a
a.append(4)  # Modify a in-place
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4], b is affected because it points to the same object
print(a is b)  # True: a and b are the same object
````
If you create a new object, even though the content seems similar, the identity will be different:
````python
a = [1, 2, 3]
b = a
a = a + [4]  # a points to a new list
print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3]
print(a is b)  # False: a and b now point to different objects
````
## 4) Immutable Objects

Immutable objects cannot be modified once created. Examples of immutable objects in Python include strings, tuples, and integers. Any operation that seems like a modification actually creates a new object.

For example:
````python
a = 5
b = a
a += 1  # This creates a new object with value 6, leaving a as 5
print(a)  # 6
print(b)  # 5
print(a is b)  # False: a and b point to different objects now
````
For tuples (which are immutable containers), the structure itself cannot be changed, but mutable objects within the tuple can be modified:
````
t = ([1, 2, 3], 4)
t[0].append(5)  # Modifies the list inside the tuple
print(t)  # ([1, 2, 3, 5], 4), the tuple is immutable, but the list inside it is not
````
In this case, the tuple remains unchanged, but the list inside it is mutable, so its contents can change.

## 5) Why Does It Matter? How Python Treats Mutable and Immutable Objects Differently

Understanding how mutable and immutable objects work is crucial for predicting how your code will behave, especially when passing objects to functions or assigning them to new variables.
In-Place vs Out-of-Place Modifications

The behavior of mutable vs immutable objects impacts operations:
| Operation             | Behavior                   | New Object Created? |
|-----------------------|----------------------------|----------------------|
| `a += [4]` (list)     | In-place modification       | No                   |
| `a = a + [4]` (list)  | Out-of-place (new object)   | Yes                  |
| `a += 1` (int)        | New object created          | Yes                  |

### Function Arguments

When passing objects to functions, mutable objects can be modified, but immutable objects cannot.
````python
def add_to_list(lst):
    lst.append(4)  # Modifies the list in-place

my_list = [1, 2, 3]
add_to_list(my_list)
print(my_list)  # [1, 2, 3, 4]

def increment(x):
    x += 1  # Creates a new integer object

a = 10
increment(a)
print(a)  # 10, the original value of a remains unchanged
````
## 6) How Arguments Are Passed to Functions

Python uses pass-by-object-reference, meaning it passes the reference to the object, not the actual object itself. This is important because:

- For **mutable objects**, changes inside the function affect the original object.

- For **immutable objects**, changes inside the function do not affect the original object; a new one is created.

Example with a mutable object:
````python
def add_to_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
add_to_list(my_list)
print(my_list)  # [1, 2, 3, 4]

Example with an immutable object:

def increment(x):
    x += 1

a = 10
increment(a)
print(a)  # 10, the original value of a remains unchanged
````
## 7) Python Interning and Singleton

Python has a concept of interning where certain objects are stored in memory once and reused. This is common for small integers (from -5 to 256) and certain strings. This behavior helps with memory efficiency and improves performance.
````python
a = 100
b = 100
print(a is b)  # True, because small integers are cached
````
However, larger integers are not interned:
````python
a = 257
b = 257
print(a is b)  # False, because 257 is not in the cached range
````
Singletons refer to values where only one instance exists in memory. Some examples are None, True, False, and empty tuples ().
````python
a = ()
b = ()
print(a is b)  # True, because empty tuples are singleton objects in memory
````
## 8) Garbage Collector

Python automatically manages memory through the garbage collector (GC). When an object is no longer referenced, Python will remove it from memory. This is especially important for large programs where memory management becomes critical.

For example, when a new list is created by modifying an existing list, the old list becomes unreferenced and eligible for garbage collection:
````python
l1 = [1, 2, 3]
l1 = l1 + [4]  # l1 points to a new list, old list is unreferenced
````
## Conclusion

In this blog, we've explored the differences between mutable and immutable objects in Python. Understanding how these objects are managed in memory and how they behave when passed to functions or assigned to new variables is essential for writing efficient, bug-free code. By knowing how Python handles object identity and mutability, you can avoid common pitfalls and make more predictable decisions in your code.
