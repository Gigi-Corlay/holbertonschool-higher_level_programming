# Python OOP – Advanced Concepts

## 📌 Description

This project aims to strengthen advanced **Object-Oriented Programming (OOP) concepts in Python**.  
It focuses on designing robust, extensible, and maintainable classes using abstract classes, interfaces, multiple inheritance, and mixins.

---

## 🎯 Learning Objectives

By the end of this project, you should be able to:

- Understand and apply **abstract classes** to define common interfaces while enforcing a certain level of class completeness.
- Grasp the concept of **interfaces and duck typing** to ensure that objects adhere to a specific contract or protocol.
- Extend **standard base classes** (`list`, `dict`, `iterator`, etc.) to create custom data structures with specialized behavior.
- Use **method overriding** to modify or enhance the behavior of inherited methods.
- Understand and apply **multiple inheritance** to form complex relationships between classes.
- Use **mixins** to compose reusable behavior across unrelated classes.

---

## 🧱 Concepts Covered

### 1️⃣ Abstract Classes
Abstract classes are used to define methods that must be implemented by subclasses.  
They help enforce a common structure and prevent instantiation of incomplete classes.

➡️ Implemented using the `abc` module and the `@abstractmethod` decorator.

---

### 2️⃣ Interfaces and Duck Typing
Python does not provide explicit interfaces like some other languages. Instead, it relies on:
- **Abstract base classes** for strict interface enforcement
- **Duck typing**, which focuses on behavior rather than type

> *“If it looks like a duck and quacks like a duck, it’s a duck.”*

---

### 3️⃣ Subclassing Standard Base Classes
Python allows inheritance from built-in types such as:
- `list`
- `dict`
- `iterator`

This enables the creation of custom data structures while retaining native Python functionality.

---

### 4️⃣ Method Overriding
Method overriding allows a subclass to:
- Replace a parent class method
- Extend its behavior using `super()`

This is essential for adapting inherited behavior to specific needs.

---

### 5️⃣ Multiple Inheritance
Multiple inheritance allows a class to inherit from more than one parent class.  
Python uses a **Method Resolution Order (MRO)** to determine how methods are resolved.

⚠️ Understanding MRO is crucial to avoid conflicts.

---

### 6️⃣ Mixins
Mixins are lightweight classes designed to add specific functionality to other classes.  
They:
- Are not meant to be instantiated on their own
- Promote code reuse
- Help avoid deep and complex inheritance hierarchies

---
