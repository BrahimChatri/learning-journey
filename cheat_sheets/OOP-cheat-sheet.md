
# OOP in Python Cheat Sheet

#### 1. **Classes and Objects**
- **Class**: A blueprint for creating objects. Classes define properties (attributes) and methods (functions).
    ```python
    class Dog:
        def __init__(self, name, age):  # Constructor
            self.name = name  # Attribute
            self.age = age    # Attribute

        def bark(self):  # Method
            return "Woof!"

    # Object
    my_dog = Dog("Buddy", 3)
    print(my_dog.bark())  # Output: Woof!
    ```

- **Object**: An instance of a class. Objects have states (attributes) and behaviors (methods).

#### 2. **Attributes and Methods**
- **Attributes**: Variables that belong to a class (class attributes) or an instance (instance attributes).
- **Methods**: Functions defined within a class that describe the behaviors of an object.
    - **Instance Methods**: Operate on an instance of the class.
    - **Class Methods**: Use `@classmethod` decorator, operate on the class itself. Defined with `cls`.
    - **Static Methods**: Use `@staticmethod` decorator, do not access or modify class state.

    ```python
    class MyClass:
        class_variable = "I am a class variable"

        def __init__(self, instance_variable):
            self.instance_variable = instance_variable

        @classmethod
        def class_method(cls):
            return cls.class_variable

        @staticmethod
        def static_method():
            return "I am a static method"
    ```

#### 3. **Inheritance**
- **Inheritance**: Mechanism of basing a class (child class) on another class (parent class), inheriting attributes and methods.
    ```python
    class Animal:
        def speak(self):
            return "Animal speaks"

    class Dog(Animal):  # Dog inherits from Animal
        def speak(self):  # Overriding the parent method
            return "Woof!"
    
    my_dog = Dog()
    print(my_dog.speak())  # Output: Woof!
    ```

- **Types of Inheritance**:
  - Single, Multiple, Multilevel, Hierarchical, Hybrid.

#### 4. **Polymorphism**
- **Polymorphism**: The ability to define methods in the child class with the same name as defined in their parent class. Achieved through method overriding.
    ```python
    class Cat(Animal):
        def speak(self):
            return "Meow!"

    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())  # Output: Woof! Meow!
    ```

#### 5. **Encapsulation**
- **Encapsulation**: Restricting access to some of the object's components. Achieved using private (single `_`) and protected (double `__`) attributes.
    ```python
    class Person:
        def __init__(self, name):
            self._name = name  # Protected attribute

        def get_name(self):
            return self._name

    person = Person("Alice")
    print(person.get_name())  # Output: Alice
    ```

#### 6. **Abstraction**
- **Abstraction**: Hiding complex implementation details and showing only essential features of an object. Achieved using abstract base classes.
    ```python
    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def speak(self):
            pass

    class Dog(Animal):
        def speak(self):
            return "Woof!"
    ```

#### 7. **Dunder (Magic) Methods**
- **Dunder Methods**: Special methods with double underscores (e.g., `__init__`, `__str__`, `__repr__`) that enable operator overloading and provide special functionality.
    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return f"Point({self.x}, {self.y})"
    ```

#### 8. **Properties with `@property` Decorator**
- **`@property`**: A decorator to define getters and setters, allowing controlled access to private attributes.
    ```python
    class Employee:
        def __init__(self, salary):
            self._salary = salary

        @property
        def salary(self):
            return self._salary

        @salary.setter
        def salary(self, value):
            if value > 0:
                self._salary = value
    ```

#### 9. **Important Concepts**
- **Aggregation**: A "has-a" relationship where a class contains a reference to another class.
- **Composition**: Strong form of aggregation where the contained object is owned by the containing object.

### Summary
- **OOP Principles**: Encapsulation, Abstraction, Inheritance, Polymorphism.
- **Key Concepts**: Class, Object, Method, Attribute, Inheritance Types, Method Overriding, Dunder Methods, `@property`.

