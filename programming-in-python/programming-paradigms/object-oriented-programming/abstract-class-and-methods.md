# Abstract classes and methods

Here's a summary of the key points about abstract classes and methods from the text:

1. **Abstract Classes**:
   - An abstract class is a type of class that cannot be instantiated directly.
   - It serves as a blueprint for other classes, enforcing that certain methods must be implemented in derived classes.

2. **Purpose of Abstract Classes**:
   - To ensure consistency and avoid code duplication by requiring derived classes to implement specified methods.
   - They hide implementation details while exposing a consistent interface.

3. **Abstract Methods**:
   - Methods defined in an abstract class that must be implemented by any derived class.
   - They cannot be called directly on instances of the abstract class but must be overridden in derived classes.

4. **Python Implementation**:
   - Python does not support abstract classes natively; they must be defined using the `abc` (Abstract Base Classes) module.
   - The `ABC` module provides the base class for defining abstract classes.
   - The `abstractmethod` decorator is used to define abstract methods.

5. **Creating an Abstract Class**:
   - Import the `ABC` module and use it to create an abstract class.
   - Define abstract methods using the `@abstractmethod` decorator.

6. **Example**:
   - An abstract class `Employee` with an abstract method `donate`.
   - A derived class `Donation` that implements the `donate` method.
   - Instances of the derived class can use the implemented methods, but instances of the abstract class cannot.

7. **Practical Application**:
   - In the example, the abstract class helps to structure a program for collecting donations, ensuring that all derived classes implement the `donate` method.

By using abstract classes and methods, you can design a more robust and maintainable codebase, ensuring that all necessary methods are implemented in derived classes while keeping the implementation details hidden.

## Example

Certainly! Here's a simple example of how to use abstract classes and methods in Python:

```python
from abc import ABC, abstractmethod

# Define an abstract class
class Employee(ABC):
    
    @abstractmethod
    def donate(self):
        pass

# Define a concrete class that inherits from the abstract class
class Donation(Employee):
    
    def donate(self):
        # Implementation of the abstract method
        amount = float(input("Enter donation amount: "))
        return amount

# Create instances of the concrete class
john = Donation()
peter = Donation()

# Call the donate method
john_donation = john.donate()
peter_donation = peter.donate()

# Collect the donation amounts
amounts = [john_donation, peter_donation]

# Print total donations
print(f"Total donations: {sum(amounts)}")
```

### Explanation:

1. **Abstract Class**:
   - `Employee` is an abstract class derived from `ABC`.
   - It contains an abstract method `donate()` which must be implemented by any derived class.

2. **Concrete Class**:
   - `Donation` inherits from `Employee` and provides the implementation for the `donate` method.
   - This method prompts the user to enter a donation amount and returns it.

3. **Instantiation and Usage**:
   - Instances of the `Donation` class are created (`john` and `peter`).
   - The `donate` method is called on each instance to get donation amounts.
   - The total donations are computed and printed.

This example demonstrates how abstract classes ensure that derived classes implement specific methods while allowing those methods to be defined in a flexible manner.

## Quiz

1. The correct answer is:

**Function called abstract**

In Python, the requirements to create an abstract method are:

- **Use of a decorator called `abstractmethod`**: This decorator is used to define an abstract method within an abstract class.
- **A module called `abc`**: This module provides the `ABC` class and the `abstractmethod` decorator for creating abstract classes and methods.

The other options, such as a function called `ABC` or `abstract`, are not relevant to the creation of abstract methods.

1. **False**

Python does not support direct implementation of abstraction in the same way that some other languages do. Instead, abstraction in Python is implemented using the `abc` (Abstract Base Classes) module, which provides the `ABC` class and the `abstractmethod` decorator. This approach allows you to define abstract classes and methods, but it requires using the `abc` module rather than having built-in, direct support for abstraction.

1. The OOP principle majorly used by Python to perform abstraction is:

**Inheritance**

In Python, abstraction is achieved through inheritance by creating abstract base classes (using the `ABC` class and `abstractmethod` decorator) that define methods that must be implemented by derived classes. This allows you to define a common interface and hide implementation details in the base class, while the specific details are handled in the subclasses.

1. The correct statement about abstract classes is:

**Abstract classes act only as a base class for other classes to derive from.**

Abstract classes are designed to be inherited by other classes and provide a common interface. They cannot be instantiated directly and are used to define methods that must be implemented by derived classes.

1. **False**

Abstract classes in Python can exist without abstract methods. An abstract class can be defined simply to provide a common base class for other classes, even if it does not have any abstract methods. The primary purpose of an abstract class is to serve as a blueprint for derived classes, but it is not required to have abstract methods to fulfill that role.