# 🐍 Python – Classes and Objects

## 📚 Table of Contents
1. [🧩 What is OOP?](#-what-is-oop)
2. [✨ “First-class everything”](#-first-class-everything)
3. [🏗️ What is a class?](#-what-is-a-class)
4. [👤 What is an object and an instance?](#-what-is-an-object-and-an-instance)
5. [⚖️ Difference between class and object/instance](#-difference-between-class-and-objectinstance)
6. [📦 What is an attribute?](#-what-is-an-attribute)
7. [🔒 Public, protected, and private attributes](#-public-protected-and-private-attributes)
8. [🙋 What is `self`?](#-what-is-self)
9. [⚙️ What is a method?](#-what-is-a-method)
10. [🚀 What is the special `__init__` method?](#-what-is-the-special-init-method)
11. [🛡️ Data Abstraction, Encapsulation, and Information Hiding](#-data-abstraction-encapsulation-and-information-hiding)
12. [🏷️ What is a property?](#-what-is-a-property)
13. [🔑 Difference between an attribute and a property](#-difference-between-an-attribute-and-a-property)
14. [🐍 Pythonic way to write getters and setters](#-pythonic-way-to-write-getters-and-setters)
15. [⚡ Dynamically creating new attributes](#-dynamically-creating-new-attributes)
16. [🔗 Binding attributes to objects and classes](#-binding-attributes-to-objects-and-classes)
17. [📖 `__dict__` of a class and instance](#-dict-of-a-class-and-instance)
18. [🧭 How Python finds attributes](#-how-python-finds-attributes)
19. [🎯 Using `getattr`](#-using-getattr)

---

## 🧩 What is OOP?
**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code around **objects** rather than procedures.  

- Objects combine **data (attributes)** and **behavior (methods)**.
- Main principles: **Encapsulation, Abstraction, Inheritance, Polymorphism**.

---

## ✨ “First-class everything”
In Python, functions, classes, and even modules are **first-class objects**, meaning they can be:

- 📝 Assigned to variables  
- 📦 Passed as arguments to functions  
- 🔄 Returned from functions  
- 💾 Stored in data structures

---

## 🏗️ What is a class?
A **class** is a **blueprint or template** for creating objects.  

```python
class User:
    pass
