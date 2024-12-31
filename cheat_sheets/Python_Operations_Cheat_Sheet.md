# Python Operations Cheat Sheet

## 1. **Arithmetic Operations**
Perform mathematical calculations.

| Operation        | Symbol | Example        | Output |
|------------------|--------|----------------|--------|
| Addition         | `+`    | `3 + 2`        | `5`    |
| Subtraction      | `-`    | `5 - 2`        | `3`    |
| Multiplication   | `*`    | `4 * 3`        | `12`   |
| Division         | `/`    | `10 / 2`       | `5.0`  |
| Floor Division   | `//`   | `7 // 2`       | `3`    |
| Modulus          | `%`    | `7 % 2`        | `1`    |
| Exponentiation   | `**`   | `2 ** 3`       | `8`    |

---

## 2. **Comparison Operations**
Compare two values, returning `True` or `False`.

| Operation        | Symbol | Example         | Output  |
|------------------|--------|-----------------|---------|
| Equal to         | `==`   | `5 == 5`        | `True`  |
| Not equal to     | `!=`   | `5 != 3`        | `True`  |
| Greater than     | `>`    | `7 > 3`         | `True`  |
| Less than        | `<`    | `3 < 5`         | `True`  |
| Greater or equal | `>=`   | `7 >= 7`        | `True`  |
| Less or equal    | `<=`   | `4 <= 9`        | `True`  |

---

## 3. **Logical Operations**
Combine conditional statements.

| Operation | Symbol/Keyword | Example                  | Output  |
|-----------|----------------|--------------------------|---------|
| AND       | `and`          | `True and False`         | `False` |
| OR        | `or`           | `True or False`          | `True`  |
| NOT       | `not`          | `not True`               | `False` |

---

## 4. **Assignment Operations**
Assign or update values.

| Operation          | Symbol  | Example      | Output            |
|--------------------|---------|--------------|-------------------|
| Assignment         | `=`     | `x = 5`      | `x = 5`          |
| Add and assign     | `+=`    | `x += 3`     | `x = x + 3`      |
| Subtract and assign| `-=`    | `x -= 2`     | `x = x - 2`      |
| Multiply and assign| `*=`    | `x *= 2`     | `x = x * 2`      |
| Divide and assign  | `/=`    | `x /= 2`     | `x = x / 2`      |
| Modulus and assign | `%=`    | `x %= 3`     | `x = x % 3`      |
| Floor Div and assign| `//=`  | `x //= 2`    | `x = x // 2`     |
| Exponent and assign| `**=`   | `x **= 2`    | `x = x ** 2`     |

---

## 5. **Membership Operations**
Check if a value exists in a sequence.

| Operation    | Symbol | Example               | Output  |
|--------------|--------|-----------------------|---------|
| In           | `in`   | `'a' in 'apple'`      | `True`  |
| Not in       | `not in` | `'z' not in 'apple'` | `True`  |

---

## 6. **Identity Operations**
Compare objects’ memory locations.

| Operation    | Symbol   | Example            | Output  |
|--------------|----------|--------------------|---------|
| Is           | `is`     | `x is y`           | `True` (if same object) |
| Is not       | `is not` | `x is not y`       | `True` (if different objects) |

---

## 7. **Bitwise Operations**
Perform binary computations.

| Operation      | Symbol | Example       | Binary Output             |
|----------------|--------|---------------|---------------------------|
| AND            | `&`    | `5 & 3`       | `1` (0101 & 0011 = 0001)  |
| OR             | `|`    | `5 | 3`       | `7` (0101 | 0011 = 0111)  |
| XOR            | `^`    | `5 ^ 3`       | `6` (0101 ^ 0011 = 0110)  |
| Left Shift     | `<<`   | `5 << 1`      | `10` (0101 << 1 = 1010)   |
| Right Shift    | `>>`   | `5 >> 1`      | `2` (0101 >> 1 = 0010)    |

---

## 8. **String Operations**
Strings have unique operations.

| Operation           | Example                        | Output       |
|---------------------|--------------------------------|--------------|
| Concatenation       | `'Hello' + ' World'`          | `'Hello World'` |
| Repetition          | `'Hi' * 3`                    | `'HiHiHi'`   |
| Length              | `len('Hello')`                | `5`          |
| Indexing            | `'Python'[0]`                 | `'P'`        |
| Slicing             | `'Python'[1:4]`               | `'yth'`      |

---

## 9. **Common Built-in Functions for Operations**
Useful functions for data manipulation.

| Function      | Description                        | Example             | Output |
|---------------|------------------------------------|---------------------|--------|
| `abs(x)`      | Absolute value                    | `abs(-5)`           | `5`    |
| `pow(x, y)`   | Raise to power (x^y)             | `pow(2, 3)`         | `8`    |
| `round(x)`    | Round to nearest integer          | `round(3.6)`        | `4`    |
| `max(x, y, z)`| Find maximum                      | `max(1, 5, 3)`      | `5`    |
| `min(x, y, z)`| Find minimum                      | `min(1, 5, 3)`      | `1`    |
| `sum()`       | Sum of iterable                   | `sum([1, 2, 3])`    | `6`    |

---

This cheat sheet covers the essential Python operations. Let me know if you need examples or explanations for any specific part!

