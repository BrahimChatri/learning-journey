
## Python Dunder (Magic) Methods Cheat Sheet with Code  Examples


#### 1. **Initialization and Representation Methods**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age})"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __del__(self):
        print(f"Deleting {self.name}'s instance.")
        
# Example usage
p = Person("Alice", 30)
print(repr(p))   # Output: Person(name='Alice', age=30)
print(str(p))    # Output: Alice is 30 years old.
del p            # Output: Deleting Alice's instance.
```

#### 2. **Attribute Access Methods**

```python
class Sample:
    def __init__(self):
        self.existing_attribute = "I exist!"

    def __getattr__(self, name):
        return f"{name} attribute not found!"

    def __getattribute__(self, name):
        print(f"Accessing {name} attribute...")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

    def __delattr__(self, name):
        print(f"Deleting attribute {name}")
        super().__delattr__(name)
        
# Example usage
s = Sample()
print(s.existing_attribute)  # Output: Accessing existing_attribute attribute... \n I exist!
print(s.non_existing)        # Output: non_existing attribute not found!
s.new_attribute = "New!"     # Output: Setting new_attribute to New!
del s.new_attribute          # Output: Deleting attribute new_attribute
```

#### 3. **Operator Overloading Methods**

##### Arithmetic Operators

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2            # Output: Vector(4, 6)
v4 = v1 * 3             # Output: Vector(3, 6)
print(v3)
print(v4)
```

##### In-place Arithmetic Operators

```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __iadd__(self, other):
        self.value += other
        return self
    
    def __imul__(self, other):
        self.value *= other
        return self
    
    def __repr__(self):
        return f"Number({self.value})"

# Example usage
n = Number(5)
n += 3  # Output: Number(8)
n *= 2  # Output: Number(16)
print(n)
```

##### Bitwise Operators

```python
class Bitwise:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return Bitwise(self.value & other.value)

    def __or__(self, other):
        return Bitwise(self.value | other.value)

    def __xor__(self, other):
        return Bitwise(self.value ^ other.value)

    def __repr__(self):
        return f"Bitwise({self.value})"

# Example usage
a = Bitwise(0b1100)
b = Bitwise(0b1010)
print(a & b)  # Output: Bitwise(8)
print(a | b)  # Output: Bitwise(14)
print(a ^ b)  # Output: Bitwise(6)
```

#### 4. **Comparison Operators**

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area() == other.area()
    
    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
    
# Example usage
r1 = Rectangle(3, 4)
r2 = Rectangle(6, 2)
r3 = Rectangle(4, 4)
print(r1 == r2)  # Output: True
print(r1 < r3)   # Output: True
print(r2 <= r3)  # Output: True
```

#### 5. **Container and Sequence Methods**

```python
class CustomList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]
    
    def __iter__(self):
        return iter(self.data)
    
# Example usage
clist = CustomList()
clist.data = [1, 2, 3, 4]
print(len(clist))  # Output: 4
print(clist[2])    # Output: 3
clist[2] = 10      # Sets the third element to 10
print(clist[2])    # Output: 10
del clist[2]       # Deletes the third element
print(list(clist)) # Output: [1, 2, 4]
```

#### 6. **Callable and Context Manager Methods**

```python
class Adder:
    def __init__(self, value):
        self.value = value
    
    def __call__(self, x):
        return self.value + x

# Example usage
add_five = Adder(5)
print(add_five(10))  # Output: 15

class Resource:
    def __enter__(self):
        print("Entering context...")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context...")

# Example usage
with Resource() as r:
    print("Inside the context.")
# Output: Entering context... \n Inside the context. \n Exiting context...
```

#### 7. **Type Conversion Methods**

```python
class Example:
    def __init__(self, value):
        self.value = value
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __bool__(self):
        return bool(self.value)

# Example usage
ex = Example(10)
print(int(ex))   # Output: 10
print(float(ex)) # Output: 10.0
print(bool(ex))  # Output: True
```

#### 8. **Other Special Methods**

```python
class HashableObject:
    def __init__(self, value):
        self.value = value
    
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other):
        return self.value == other.value

# Example usage
obj1 = HashableObject(5)
obj2 = HashableObject(5)
print(hash(obj1))  # Output: Hash value of 5
print(obj1 == obj2)  # Output: True
```

#### 9. **Advanced Customization**

```python
class MyDict(dict):
    def __missing__(self, key):
        return f"{key} not found!"

# Example usage
my_dict = MyDict(a=1, b=2)
print(my_dict['a'])  # Output: 1
print(my_dict['c'])  # Output: c not found!
```

