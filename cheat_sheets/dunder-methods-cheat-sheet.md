
## Python Dunder (Magic) Methods Cheat Sheet


#### 1. **Initialization and Representation Methods**

- `__init__(self, ...)`: Constructor method; called when an instance of the class is created. It initializes the object's attributes.
  
- `__new__(cls, ...)`: Allocates memory for a new object; called before `__init__()`.

- `__del__(self)`: Destructor method; called when an instance is about to be destroyed.

- `__repr__(self)`: Called by the `repr()` function; provides a "formal" string representation of the object that could be used to recreate the object.

- `__str__(self)`: Called by the `str()` function and `print()`; provides an "informal" or nicely printable string representation of the object.

- `__bytes__(self)`: Called by the `bytes()` function; converts an object to bytes.

- `__format__(self, format_spec)`: Called by `format()` and `str.format()`, used to customize string formatting.

#### 2. **Attribute Access Methods**

- `__getattr__(self, name)`: Called when trying to access an attribute that doesn’t exist.

- `__getattribute__(self, name)`: Called when any attribute is accessed; to override, you must explicitly call `super().__getattribute__(name)`.

- `__setattr__(self, name, value)`: Called when an attribute assignment is attempted. 

- `__delattr__(self, name)`: Called when an attribute deletion is attempted.

- `__dir__(self)`: Called by `dir()`; returns a list of attributes and methods.

#### 3. **Operator Overloading Methods**

##### Arithmetic Operators

- `__add__(self, other)`: Implements addition (`+`).

- `__sub__(self, other)`: Implements subtraction (`-`).

- `__mul__(self, other)`: Implements multiplication (`*`).

- `__truediv__(self, other)`: Implements division (`/`).

- `__floordiv__(self, other)`: Implements floor division (`//`).

- `__mod__(self, other)`: Implements modulus (`%`).

- `__pow__(self, other[, modulo])`: Implements exponentiation (`**`).

- `__matmul__(self, other)`: Implements matrix multiplication (`@`).

##### In-place Arithmetic Operators

- `__iadd__(self, other)`: Implements in-place addition (`+=`).

- `__isub__(self, other)`: Implements in-place subtraction (`-=`).

- `__imul__(self, other)`: Implements in-place multiplication (`*=`).

- `__itruediv__(self, other)`: Implements in-place division (`/=`).

- `__ifloordiv__(self, other)`: Implements in-place floor division (`//=`).

- `__imod__(self, other)`: Implements in-place modulus (`%=`).

- `__ipow__(self, other[, modulo])`: Implements in-place exponentiation (`**=`).

- `__imatmul__(self, other)`: Implements in-place matrix multiplication (`@=`).

##### Bitwise Operators

- `__and__(self, other)`: Implements bitwise AND (`&`).

- `__or__(self, other)`: Implements bitwise OR (`|`).

- `__xor__(self, other)`: Implements bitwise XOR (`^`).

- `__lshift__(self, other)`: Implements left shift (`<<`).

- `__rshift__(self, other)`: Implements right shift (`>>`).

##### In-place Bitwise Operators

- `__iand__(self, other)`: Implements in-place bitwise AND (`&=`).

- `__ior__(self, other)`: Implements in-place bitwise OR (`|=`).

- `__ixor__(self, other)`: Implements in-place bitwise XOR (`^=`).

- `__ilshift__(self, other)`: Implements in-place left shift (`<<=`).

- `__irshift__(self, other)`: Implements in-place right shift (`>>=`).

#### 4. **Comparison Operators**

- `__eq__(self, other)`: Implements equality comparison (`==`).

- `__ne__(self, other)`: Implements inequality comparison (`!=`).

- `__lt__(self, other)`: Implements less-than comparison (`<`).

- `__le__(self, other)`: Implements less-than-or-equal-to comparison (`<=`).

- `__gt__(self, other)`: Implements greater-than comparison (`>`).

- `__ge__(self, other)`: Implements greater-than-or-equal-to comparison (`>=`).

#### 5. **Container and Sequence Methods**

- `__len__(self)`: Called by `len()`; returns the length of the container.

- `__getitem__(self, key)`: Called to retrieve an item (e.g., `self[key]`).

- `__setitem__(self, key, value)`: Called to set an item (e.g., `self[key] = value`).

- `__delitem__(self, key)`: Called to delete an item (e.g., `del self[key]`).

- `__iter__(self)`: Called by `iter()`; returns an iterator object.

- `__next__(self)`: Called by `next()`; returns the next item from the iterator.

- `__reversed__(self)`: Called by `reversed()`; returns a reverse iterator.

- `__contains__(self, item)`: Called by the `in` operator to check membership.

#### 6. **Callable and Context Manager Methods**

- `__call__(self, *args, **kwargs)`: Makes an instance callable like a function.

- `__enter__(self)`: Called at the beginning of a `with` statement block.

- `__exit__(self, exc_type, exc_value, traceback)`: Called at the end of a `with` statement block to handle cleanup.

#### 7. **Type Conversion Methods**

- `__int__(self)`: Called by `int()`; converts the object to an integer.

- `__float__(self)`: Called by `float()`; converts the object to a float.

- `__complex__(self)`: Called by `complex()`; converts the object to a complex number.

- `__bool__(self)`: Called by `bool()`; converts the object to a boolean.

- `__index__(self)`: Called by built-in functions like `bin()`, `hex()`, and `oct()`; converts the object to an integer.

#### 8. **Other Special Methods**

- `__hash__(self)`: Called by `hash()`; returns an integer hash value for an object.

- `__copy__(self)`: Called by the `copy` module to create a shallow copy of an object.

- `__deepcopy__(self, memodict={})`: Called by the `copy` module to create a deep copy of an object.

- `__sizeof__(self)`: Called by `sys.getsizeof()`; returns the size of the object in bytes.

#### 9. **Advanced Customization**

- `__missing__(self, key)`: Only for subclasses of `dict`. Called by `dict` if a key is not found.

- `__set_name__(self, owner, name)`: Called automatically when the instance is assigned to a class attribute. 

### Conclusion

Dunder methods provide a powerful way to control object behavior and make your classes more intuitive and Pythonic. Understanding how to use and implement them effectively is crucial for writing idiomatic Python code.