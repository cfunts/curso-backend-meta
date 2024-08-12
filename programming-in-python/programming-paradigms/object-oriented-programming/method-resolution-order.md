# Method Resolution Order

Here are the key notes from the text:

1. **Method Resolution Order (MRO)**: MRO is a set of rules that determines the order in which methods and attributes are inherited in Python classes, particularly in complex inheritance scenarios. It helps in understanding how methods are resolved in class hierarchies.

2. **Types of Inheritance**:
   - **Simple Inheritance**: A child class inherits from a single parent class.
   - **Multiple Inheritance**: A child class inherits from more than one parent class.
   - **Multi-Level Inheritance**: Inheritance occurs at multiple levels (e.g., class C inherits from class B, which inherits from class A).
   - **Hierarchical Inheritance**: Multiple child classes inherit from a common parent class.
   - **Hybrid Inheritance**: A combination of multiple types of inheritance.

3. **Linearization of Classes**: The order in which methods are resolved in a class hierarchy is called the linearization of a class. The MRO defines this order, which follows a bottom-to-top, left-to-right approach when visualized as a tree structure.

4. **Python's MRO Algorithm**:
   - Old-style classes used Depth First Search (DFS).
   - New-style classes (from Python 3 onwards) use the C3 Linearization algorithm, which follows monotonicity (inherited properties cannot skip direct parents) and visits the superclass methods only after local class methods.

5. **MRO Functions**:
   - The `MRO` function in Python can be used to determine the order of method resolution in a class.
   - The `help` function provides detailed information, including MRO, data descriptors, and types used in the code.

6. **Importance of MRO**: Understanding MRO is crucial for managing complex class hierarchies and ensuring that methods and attributes are inherited in a predictable manner.

## Example

Here’s an example illustrating how Method Resolution Order (MRO) works in Python:

### Scenario:
Let's say you have three classes: `A`, `B`, and `C`. 
- `B` inherits from `A`.
- `C` inherits from `B`.

```python
class A:
    def __init__(self):
        self.num = 5

    def display(self):
        print("Class A")

class B(A):
    def __init__(self):
        self.num = 9

    def display(self):
        print("Class B")

class C(B):
    def display(self):
        print("Class C")

# Creating an instance of class C
c = C()
print(c.num)  # Output: 9
c.display()   # Output: Class C
```

### Explanation:
1. **Inheritance**:
   - `Class B` inherits from `Class A`.
   - `Class C` inherits from `Class B`.

2. **MRO**:
   - When you create an instance of `C` and access `c.num`, Python follows the MRO to determine from which class to inherit the `num` attribute.
   - The MRO for class `C` is: `C -> B -> A`.
   - Since `B` has an `__init__` method that assigns `self.num = 9`, this value is inherited by `C`.

3. **Method Resolution**:
   - When you call `c.display()`, Python follows the MRO to find the `display` method.
   - The MRO dictates that `C.display()` is used, so "Class C" is printed.

### MRO Function:
You can check the MRO of class `C` using the `mro()` function:

```python
print(C.mro())
```

### Output:
```python
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
```

This shows the MRO for `C`, confirming that Python will first look in `C`, then `B`, then `A`, and finally the base `object` class if needed.

### Use of `help` Function:
If you want more detailed information, you can use the `help()` function:

```python
help(C)
```

This will give you a detailed breakdown of the MRO, along with other information about `C`, including its methods and attributes.

### Complex Example with Multiple Inheritance:
If we add another parent class `D` and modify `C` to inherit from both `B` and `D`, the MRO becomes more complex:

```python
class D:
    def display(self):
        print("Class D")

class C(B, D):
    pass

# Creating an instance of class C
c = C()
c.display()  # Output: Class B
```

### MRO in this Case:
- The MRO will now be: `C -> B -> D -> A`.
- Even though `D` is a parent of `C`, the method from `B` is resolved first due to the left-to-right order in the MRO.

By understanding the MRO, you can predict and control which methods and attributes are inherited in complex class hierarchies.



