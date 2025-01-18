# Python Basics for Beginners

## Introduction
Python is a versatile and beginner-friendly programming language. This guide introduces basic Python concepts for those starting out.

---

## 1. Variables
Variables store data in Python. You don't need to declare their type explicitly.

### Example:
```python
# Creating variables
name = "Alice"    # String
age = 25           # Integer
height = 5.5       # Float
is_student = True  # Boolean
```

### Rules for Variable Names:
- Must start with a letter or underscore (_).
- Cannot start with a number.
- Can only contain alphanumeric characters and underscores.
- Case-sensitive (`Name` and `name` are different).

---

## 2. Data Types
Python has several built-in data types:

### Common Data Types:
| Type      | Example            |
|-----------|--------------------|
| String    | `"Hello"`         |
| Integer   | `42`               |
| Float     | `3.14`             |
| Boolean   | `True` or `False`  |
| List      | `[1, 2, 3]`        |
| Tuple     | `(1, 2, 3)`        |
| Dictionary| `{ "key": "value" }` |

---

## 3. Strings
Strings are sequences of characters enclosed in quotes.

### Example:
```python
# Single and double quotes
message = 'Hello'
message = "Hello"

# String concatenation
full_name = "Alice" + " " + "Smith"
print(full_name)  # Output: Alice Smith

# String interpolation (f-strings)
name = "Bob"
age = 30
print(f"My name is {name} and I am {age} years old.")
```

---

## 4. Lists
Lists are ordered, mutable collections of items.

### Example:
```python
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing items
print(fruits[0])  # Output: apple

# Modifying items
fruits[1] = "blueberry"

# Adding items
fruits.append("orange")

# Removing items
fruits.remove("cherry")

# Iterating through a list
for fruit in fruits:
    print(fruit)
```

---

## 5. Tuples
Tuples are ordered, immutable collections of items.

### Example:
```python
# Creating a tuple
colors = ("red", "green", "blue")

# Accessing items
print(colors[1])  # Output: green

# Tuples cannot be modified
# colors[1] = "yellow"  # This will raise an error
```

---

## 6. Dictionaries
Dictionaries store key-value pairs.

### Example:
```python
# Creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Accessing values
print(person["name"])  # Output: Alice

# Adding a key-value pair
person["job"] = "Engineer"

# Removing a key-value pair
person.pop("age")

# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 7. Conditional Statements
Use `if`, `elif`, and `else` to execute code based on conditions.

### Example:
```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

---

## 8. Loops
### `for` Loop:
```python
# Iterating over a list
for number in [1, 2, 3]:
    print(number)
```

### `while` Loop:
```python
# Loop until a condition is met
count = 0
while count < 3:
    print(count)
    count += 1
```

---

## 9. Functions
Functions are reusable blocks of code.

### Example:
```python
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

---

## 10. Error Handling
Handle exceptions using `try`, `except`, and optionally `finally`.

### Example:
```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
finally:
    print("Execution complete.")
```

---

## 11. Modules and Libraries
### Importing Modules:
```python
# Importing a module
import math

# Using a module
print(math.sqrt(16))  # Output: 4.0
```

### Popular Libraries:
- `math`: Mathematical functions
- `random`: Random number generation
- `os`: Operating system interactions
- `datetime`: Working with dates and times

---

## 12. File Handling
Read from and write to files.

### Example:
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Output: Hello, world!
```

---

## 13. Comments
Use comments to explain your code.

### Example:
```python
# This is a single-line comment

"""
This is a
multi-line comment
"""
```

---

## 14. Conclusion
This guide covers the basics of Python. Practice these concepts to build a strong foundation in programming. Once comfortable, explore more advanced topics like object-oriented programming, file handling, and APIs.

