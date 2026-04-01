# Python Objects & Variables — README

## 📌 What is an Object?

In Python, **everything is an object**.
An object is a piece of data stored in memory that has:

* a **type** (e.g., int, list, string)
* a **value**
* an **identity** (its unique location in memory)

---

## 📌 Class vs Object (Instance)

* A **class** is a blueprint or template used to create objects.
* An **object (instance)** is a concrete realization of a class.

```python
class Dog:
    pass

my_dog = Dog()  # object (instance) of class Dog
```

👉 Think of a class as a plan, and an object as something built from that plan.

---

## 📌 Mutable vs Immutable Objects

* **Mutable object**: can be modified after creation
* **Immutable object**: cannot be changed after creation

```python
# Mutable
my_list = [1, 2, 3]
my_list.append(4)  # modifies the same object

# Immutable
x = 5
x = x + 1  # creates a new object
```

---

## 📌 Difference Between Mutable and Immutable

| Mutable             | Immutable          |
| ------------------- | ------------------ |
| Can change          | Cannot change      |
| Same object updated | New object created |
| Example: list, dict | Example: int, str  |

---

## 📌 What is a Reference?

A **reference** is a variable that points to an object in memory.

```python
a = [1, 2, 3]
b = a  # b references the same object as a
```

---

## 📌 What is an Assignment?

Assignment means binding a variable to an object.

```python
x = 10
```

👉 This does NOT copy the object, it just creates a reference.

---

## 📌 What is an Alias?

An **alias** occurs when multiple variables refer to the same object.

```python
a = [1, 2]
b = a
```

---

## 📌 How to Know if Two Variables Are Identical

Use the `is` operator:

```python
a = [1, 2]
b = a

print(a is b)  # True
```

👉 `is` checks if both variables point to the same object.

---

## 📌 How to Know if Two Variables Are Equal

Use `==`:

```python
a = [1, 2]
b = [1, 2]

print(a == b)  # True
print(a is b)  # False
```

👉 `==` compares values, not identity.

---

## 📌 How to Display the Memory Address

Use `id()`:

```python
x = 42
print(id(x))
```

👉 In CPython, `id()` returns the memory address.

---

## 📌 Built-in Mutable Types

* list
* dict
* set
* bytearray

---

## 📌 Built-in Immutable Types

* int
* float
* bool
* str
* tuple
* frozenset
* bytes

---

## 📌 How Python Passes Variables to Functions

Python uses **pass-by-object-reference** (also called "call by sharing").

```python
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)

print(my_list)  # [1, 2, 3, 4]
```

👉 **The function receives a reference to the same object.**

**For immutable objects:**

```python
def modify_number(x):
    x = x + 1

n = 5
modify_number(n)

print(n)
```

## 👉 A new object is created instead of modifying the original.

---

## ✅ Summary

* Variables store **references**, not values
* Objects have **identity, type, and value**
* Use `is` for identity, `==` for value comparison
* Mutable objects can change, immutable ones cannot
* Python passes references to functions

---
