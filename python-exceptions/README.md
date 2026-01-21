# 🐍 Python - Exceptions

## 📚 Project Overview

This project explores **errors and exceptions in Python**. By the end of this project, you will understand how Python handles unexpected situations and how to write robust code that gracefully manages errors.

Python is designed to be **readable, concise, and powerful**, making it easy to write code that works correctly even in edge cases. Handling exceptions is a key part of writing reliable programs.

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to explain **to anyone, without the help of Google**:

### 🌟 General

- 🐍 **Why Python programming is awesome**  
  Python is simple, expressive, and versatile. Its clear syntax and rich standard library make it ideal for beginners and experts alike.

- ⚡ **What’s the difference between errors and exceptions**  
  - ❌ **Errors:** Problems in your code that prevent Python from running it (e.g., `SyntaxError`, `IndentationError`).  
  - ⚠️ **Exceptions:** Problems that occur **during program execution** (e.g., `ZeroDivisionError`, `FileNotFoundError`).

- 🛠️ **What are exceptions and how to use them**  
  Exceptions are signals that something went wrong during execution. They can be **caught and handled** to prevent program crashes.

- ⏰ **When do we need to use exceptions**  
  - When input or operations might fail (e.g., user enters wrong data).  
  - When working with files, networks, or databases where errors are common.  
  - Whenever we want to **control the flow of the program** even in error situations.

- ✅ **How to correctly handle an exception**  
  Use `try` / `except` blocks:
  ```python
  try:
      x = int(input("Enter a number: "))
      result = 10 / x
  except ValueError:
      print("That is not a valid number.")
  except ZeroDivisionError:
      print("Cannot divide by zero.")

## ✅ Practical Summary
- **Errors** block the code (e.g., `SyntaxError`)
- **Exceptions** can be handled (e.g., `ZeroDivisionError`)
- `try / except / else / finally` allows you to **control your program** and ensure certain actions are always executed, even in case of an error.