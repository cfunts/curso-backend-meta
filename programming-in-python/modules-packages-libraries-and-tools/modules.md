# Modules

## What is a module in Python?

Here's a summary and key points about the text on Python modules:

### Summary
The text compares the flexibility of cars with the power of Python modules. Just as cars can be modified with winter tires or trailers, Python can be enhanced with modules to add functionality. Modules in Python are compared to instructions for making a pie—they provide pre-defined blocks of code that can be reused to add functionality without rewriting code.

### Key Points

1. **Functionality Enhancement**:
   - Just as cars can be modified (e.g., with winter tires), Python's functionality can be extended using modules.

2. **What is a Python Module?**:
   - A Python module is a file containing Python code, including statements and definitions (e.g., functions, variables).
   - Modules help avoid redundant code by providing reusable building blocks.

3. **Advantages of Modules**:
   - **Scope**: Modules create separate namespaces, preventing naming conflicts. Two modules can have functions with the same name without interference.
   - **Reusability**: Modules allow for code reuse, avoiding duplication and improving efficiency. For example, importing a math module gives access to pre-defined functions like factorial and GCD.
   - **Simplicity**: Modules are designed to have a specific purpose, making code simpler and easier to manage. Modules with minimal interdependencies enhance simplicity.

4. **Types of Modules**:
   - **Built-in Modules**: These are part of the standard Python library and can be accessed using `import` statements (e.g., `import math`).

5. **Importing and Executing Modules**:
   - Modules are imported once per execution. Multiple imports do not re-execute the module code; it executes only the first time.
   - Modules must be imported before any functions within them are used.
   - Modules can also be executed from within functions, allowing for dynamic use.

Overall, modules in Python are essential for organizing and reusing code efficiently, contributing to better structured and more maintainable programs.

## Accessing modules

Here are the key notes from the text:

1. **Accessing Modules in Python**:
   - Python provides access to both built-in and user-defined modules.
   - Built-in modules can be compared to pre-built construction materials (floors, walls, roofs) that simplify and speed up development.

2. **Module Search Path**:
   - Python searches for modules in the following sequence:
     1. Current directory
     2. Built-in module directory
     3. Directories listed in the Python path environment variable
     4. Installation-dependent default directory

3. **Example Code**:
   - **Creating a File**: The example starts by creating a file (`my_calendar`) and using a function to print module search paths.
   - **Importing Modules**: 
     - Importing a module (`calendar`) and using its functions.
     - Example functions from the `calendar` module:
       - `leap_days(year1, year2)`: Returns the number of leap days between two years.
       - `isleap(year)`: Returns a Boolean indicating whether a given year is a leap year.

4. **Code Execution**:
   - The example demonstrates how to print module locations and use `calendar` functions to get leap day information and check if a year is a leap year.
   - It also shows how to clean up output by iterating through locations.

5. **Exploring Modules**:
   - Users can hover over modules (using command key on Mac or Control key on Windows) to explore their functionality and dependencies.
   - The `calendar` module is located in the Python package directory and can be explored further.

6. **Best Practices**:
   - Import all required modules at the beginning of the code for clarity and organization.

This summary encapsulates the concepts and practical examples of accessing and using Python modules effectively.

## The import statement

Here's a summary and key points from the text:

1. **Import Statements and Modules**:
   - **Modules**: Any Python file (`.py` extension) is a module. For example, `check_imports.py` is a module if it is in the current working directory (scope).
   - **Importing**: You can import a module by typing `import filename` (excluding the `.py` extension). Only `.py` files can be imported; files with other extensions, like `.txt`, will not be successful.

2. **Built-in Modules**:
   - **Standard Library**: Python includes built-in modules (e.g., `json`) that come with the Python interpreter and don’t require separate installation.
   - **Using Built-in Modules**: Import them using `import module_name` and start using their functions.

3. **Packages and `__init__.py`**:
   - **Packages**: These are directories containing Python files and an `__init__.py` file. This file signals to Python that the directory should be treated as a package.
   - **Importing from Packages**: You can import modules from these directories as packages.

4. **External Packages**:
   - **PyPI**: Python Package Index (PyPI) hosts community-built packages. 
   - **Installing Packages**: Use `pip` (e.g., `pip install seaborn`) to install packages from PyPI. 
   - **Importing Installed Packages**: After installation, import them as usual (`import seaborn`).

5. **Importing from Specific Directories**:
   - **Sys Path**: Use the `sys` module to add directories to the path where Python looks for modules. 
   - **Example**: Use `sys.path.insert(0, 'path_to_directory')` to add a directory.
   - **Accessing Files**: After updating `sys.path`, you can import files from that directory (e.g., `import trial`).

6. **Practical Tips**:
   - **Local Imports**: It is generally easier to import files from the current directory. 
   - **Path Issues**: Importing modules from other directories can be tricky and specific, so it’s often best to keep files in the current working directory if possible.

Overall, the video covers the basics of importing modules in Python, using built-in and external packages, and dealing with module paths for more advanced cases.

### Example Project Structure

Assume you have the following project structure:

```
my_project/
│
├── main.py
├── utils/
│   ├── __init__.py
│   ├── helper.py
└── data/
    ├── __init__.py
    └── sample_data.py
```

### 1. Importing Modules from the Same Directory

In `main.py`, you want to import functions from `helper.py` located in the `utils` directory.

**`main.py`**:
```python
# Importing the 'function1' from 'helper.py'
from utils.helper import function1

# Using the imported function
result = function1()
print(result)
```

**`helper.py`**:
```python
def function1():
    return "Hello from helper!"
```

### 2. Importing Modules from Subdirectories

To import a module from a subdirectory, you need to ensure that the subdirectory contains an `__init__.py` file (even if it’s empty), which makes Python treat the directory as a package.

**`main.py`** (same as before):
```python
# Importing the 'function1' from 'helper.py' inside 'utils'
from utils.helper import function1

# Using the imported function
result = function1()
print(result)
```

### 3. Importing External Packages

Assume you have installed the `requests` package using `pip`.

**Installing `requests`**:
```bash
pip install requests
```

**Using `requests` in `main.py`**:
```python
import requests

response = requests.get('https://api.github.com')
print(response.status_code)
```

### 4. Importing Modules from Specific Directories Using `sys.path`

If you have a folder `workplace` with a Python file `trial.py` and want to import from it in `main.py`, you need to add the path to `sys.path`.

**`workplace/trial.py`**:
```python
names = ['Adrian', 'Maria']
```

**`main.py`**:
```python
import sys
# Adding the path to the workplace directory
sys.path.insert(0, 'path_to_workplace')

import trial

# Accessing the contents of 'trial.py'
print(trial.names)
```

In this example, replace `'path_to_workplace'` with the actual path to your `workplace` directory.

### Summary

- **Same Directory**: Import directly by the file name.
- **Subdirectories**: Ensure `__init__.py` is present and use the directory name.
- **External Packages**: Install with `pip` and import normally.
- **Specific Directories**: Use `sys.path.insert()` to add the path and import the module.

This should give you a good overview of how to handle imports in various scenarios.

## Writing import statements

Here are the key notes from the text about using modules with the `import` statement in Python:

1. **Importing Modules**:
   - To import a built-in module, use the syntax `import module_name`. For example, `import math`.
   - After importing, you can use functions from the module by prefixing them with the module name, e.g., `math.sqrt(9)`.

2. **Direct Import of Functions**:
   - Instead of importing the entire module, you can import specific functions directly with `from module_name import function_name`. For example, `from math import sqrt`.
   - This avoids loading unnecessary parts of the module and can make the code more concise.

3. **Using Aliases**:
   - You can create an alias for a module to shorten the code with `import module_name as alias_name`. For example, `import math as m`.
   - You can then use the alias to access functions, e.g., `m.cos(0)`.
   - Aliases can also be used for imported functions, e.g., `from math import factorial as f`.

4. **Importing Multiple Functions**:
   - You can import multiple functions from a module using `from module_name import function1, function2`. For example, `from math import log, sqrt`.
   - This allows selective importing of functions needed in the code.

5. **Importing All Functions**:
   - Use `from module_name import *` to import all functions from a module. For example, `from math import *`.
   - This practice can lead to confusion in large codebases, as it’s unclear where certain functions come from and can lead to potential conflicts.

6. **Importing Variables and Classes**:
   - In addition to functions, you can also import variables and classes from a module.
   - If the module does not have the specified variable or class, it will throw an error.

7. **Best Practices**:
   - Prefer specific imports over `import *` to maintain code clarity and avoid potential issues with function conflicts.
   - Use aliases to simplify code when dealing with long module names or when importing multiple functions.

These practices help in managing dependencies and organizing code efficiently.

Sure, here are examples for each of the key points:

1. **Importing Modules**:
   ```python
   import math
   result = math.sqrt(9)  # Uses the sqrt function from the math module
   print(result)  # Output: 3.0
   ```

2. **Direct Import of Functions**:
   ```python
   from math import sqrt
   result = sqrt(9)  # Directly uses the sqrt function
   print(result)  # Output: 3.0
   ```

3. **Using Aliases**:
   ```python
   import math as m
   cosine_value = m.cos(0)  # Uses the cos function from the math module with alias 'm'
   print(cosine_value)  # Output: 1.0

   from math import factorial as f
   factorial_10 = f(10)  # Uses the factorial function with alias 'f'
   print(factorial_10)  # Output: 3628800
   ```

4. **Importing Multiple Functions**:
   ```python
   from math import log, sqrt
   log_value = log(50, 10)  # Computes the base-10 logarithm of 50
   sqrt_value = sqrt(9)  # Computes the square root of 9
   print(log_value)  # Output: 1.69897 (approximately)
   print(sqrt_value)  # Output: 3.0
   ```

5. **Importing All Functions**:
   ```python
   from math import *
   log_value = log(50, 10)  # Computes the base-10 logarithm of 50
   sqrt_value = sqrt(9)  # Computes the square root of 9
   print(log_value)  # Output: 1.69897 (approximately)
   print(sqrt_value)  # Output: 3.0
   ```

6. **Importing Variables and Classes**:
   ```python
   # Let's assume we have a module named custom_module.py with a variable and a class
   # custom_module.py
   # some_variable = 42
   # class CustomClass:
   #     pass

   from custom_module import some_variable, CustomClass

   print(some_variable)  # Output: 42 (if 'some_variable' is defined in custom_module)
   instance = CustomClass()  # Creates an instance of CustomClass (if 'CustomClass' is defined in custom_module)
   ```

7. **Best Practices**:
   ```python
   # Instead of using `from math import *`, which imports all functions, use specific imports
   from math import sqrt, pi
   radius = 5
   area = pi * radius ** 2  # Uses the pi constant
   print(area)  # Output: 78.53981633974483 (approximately)
   ```

These examples illustrate how to use different import techniques and best practices in Python.

## Namespacing and scoping

Here are some key points about namespaces and scopes in Python, as explained in the text:

1. **Namespaces and Scopes**:
   - **Namespace**: A mapping from names to objects. It is essentially a container where names are mapped to their corresponding objects.
   - **Scope**: The textual region of a Python program where a namespace is directly accessible. 

2. **Module as Namespace**:
   - Every Python file is a module, and modules are a type of namespace. A module object contains names of attributes defined within it.

3. **Types of Scopes**:
   - **Local Scope**: Variables declared within a function.
   - **Enclosed Scope**: Variables in nested functions (i.e., inside an enclosing function).
   - **Global Scope**: Variables defined at the top level of a module or script.
   - **Built-in Scope**: Variables that are built into Python, such as keywords and built-in functions.

4. **Scope Resolution (LEGB Rule)**:
   - Python uses the LEGB rule to resolve variable names:
     - **Local**: First search in the local scope.
     - **Enclosed**: Then search in enclosing (non-local) scopes.
     - **Global**: Then search in the global scope.
     - **Built-in**: Finally, search in the built-in scope.

5. **Variable Identity**:
   - Each variable in Python has an identity, which is unique to its scope. The `id()` function can be used to see this identity.
   - Variables with the same name can exist in different scopes and have different identities.

6. **Implicit Declaration**:
   - Variables in Python are implicitly declared and do not require explicit datatype declaration. A variable is local unless declared as global.

7. **Global vs. Local Variables**:
   - Global variables are declared outside functions and are accessible throughout the module, but their use is discouraged due to complexity and potential for "spaghetti code."
   - Local variables are preferred for better code management and avoiding conflicts.

8. **Changing Variable Scope**:
   - **`global` Keyword**: Used to access global variables from within a function.
   - **`nonlocal` Keyword**: Used to refer to variables in an enclosing (but non-global) scope, particularly in nested functions.

9. **Code Example**:
   - In the provided example:
     - Variables named `animal` are declared at different scopes (global, local, and non-local).
     - The `nonlocal` keyword is used to modify a variable in an enclosing function's scope.

10. **Error Handling**:
    - Omitting the `nonlocal` keyword when trying to modify an enclosed variable results in an error due to the lack of a binding in the enclosing scope.

These concepts are fundamental for understanding variable management and function behavior in Python.

### Here’s an example illustrating namespaces and scopes in Python, based on the text:

```python
# Global scope
animal = 'camel'

def d():
    # Local scope of function d
    animal = 'elephant'

    def e():
        # Enclosed scope of function e
        nonlocal animal  # Refers to the variable 'animal' in the enclosing scope (function d)
        animal = 'giraffe'
        print(f"Inside nested function e: {animal}")

    print(f"Before calling function e: {animal}")
    e()  # Call the nested function
    print(f"After calling function e: {animal}")

print(f"Global scope before function call: {animal}")
d()  # Call function d
print(f"Global scope after function call: {animal}")
```

### Explanation:

1. **Global Scope**:
   - The variable `animal` is declared globally with the value `'camel'`.

2. **Function `d`**:
   - Within `d`, another local variable `animal` is declared with the value `'elephant'`.

3. **Nested Function `e`**:
   - The `nonlocal` keyword is used in `e` to indicate that `animal` refers to the `animal` variable in the enclosing function `d`, not a new local variable.
   - `e` modifies the `animal` variable to `'giraffe'`.

4. **Output**:
   - `Before calling function e`: Prints `'elephant'`, which is the value of `animal` in the local scope of `d`.
   - `Inside nested function e`: Prints `'giraffe'`, reflecting the change made by the `e` function.
   - `After calling function e`: Prints `'giraffe'`, as the change made by `e` persists in `d`'s scope.
   - `Global scope after function call`: Prints `'camel'`, unchanged by the changes in `d` and `e`.

### Sample Output:

```
Global scope before function call: camel
Before calling function e: elephant
Inside nested function e: giraffe
After calling function e: giraffe
Global scope after function call: camel
```

This example demonstrates how the `nonlocal` keyword allows nested functions to modify variables in their enclosing scope, while global variables remain unaffected.

## reload() function

Here are the key points from the text on using the `reload` function in Python:

1. **Purpose of `reload` Function**:
   - The `reload` function is used to reload an already imported module. This allows you to apply updates to the module without restarting the program.

2. **Precondition**:
   - The module passed to `reload` must already be imported. 

3. **Initial Import Behavior**:
   - Normally, Python imports a module only once per interpreter session. Subsequent imports of the same module will not reload it but will use the already loaded version.

4. **Using `reload` Function**:
   - To use `reload`, you need to import the `importlib` module. Call `importlib.reload(module)` where `module` is the module you want to reload.
   - This allows you to import the module multiple times and see changes applied.

5. **Example Demonstration**:
   - **File Creation**: 
     - Create a module `sample.py` with a simple print statement.
     - Create another file `reloads.py` to import and demonstrate the reload behavior.
   - **Directory Listing**:
     - Create `filechanges.py` to list directory contents using `os.listdir()`.
     - This file is imported and reloaded in `reloads.py` to show dynamic changes.

6. **Practical Use**:
   - **Dynamic Updates**:
     - Use `reload` to monitor changes in files and update the output dynamically without stopping the code.
   - **Example Code Execution**:
     - Update the directory contents and see changes reflected by reloading the module.
     - Modify the `filechanges.py` to include different print statements and observe changes.

7. **Implementation Details**:
   - Use a try-except block when reloading to handle any potential errors.
   - Execute a for-loop in `reloads.py` to repeatedly call a function from `filechanges.py` and demonstrate dynamic updates.

By leveraging the `reload` function, you can ensure that your program reflects changes to modules or files without having to restart the execution, making it useful for development and debugging purposes.

Sure! Here's an example demonstrating how to use the `reload` function in Python:

### Step-by-Step Example

1. **Create the Initial Module (`sample.py`)**:
   
   ```python
   # sample.py
   print("Hello world")
   ```

2. **Create the Main Script (`reloads.py`)**:
   
   ```python
   import importlib
   import sample
   
   # Reload the sample module
   importlib.reload(sample)
   ```

   - This script imports the `sample` module and then reloads it using `importlib.reload()`. If you run this script multiple times, it will print "Hello world" each time, as it reloads the module.

3. **Create a Module to List Directory Contents (`filechanges.py`)**:
   
   ```python
   # filechanges.py
   import os

   def list_directory_contents():
       current_path = os.path.dirname(__file__)
       contents = os.listdir(current_path)
       print("Contents of directory:", contents)
   ```

4. **Create a Script to Use the `filechanges` Module and Demonstrate Reloading (`reloads.py`)**:
   
   ```python
   import importlib
   import filechanges
   
   def main():
       importlib.reload(filechanges)
       filechanges.list_directory_contents()
   
   if __name__ == "__main__":
       main()
   ```

5. **Add and Remove Files to See Changes**:
   
   - **Add some text files to the directory**. For example, create `text1.txt`, `text2.txt`, and `text3.txt`.
   
   - **Run `reloads.py`** to list these files.

6. **Modify the File (`filechanges.py`) and Reload**:

   - Update `filechanges.py` to include additional information:

     ```python
     # filechanges.py
     import os

     def list_directory_contents():
         current_path = os.path.dirname(__file__)
         contents = os.listdir(current_path)
         print("Updated directory contents:")
         for item in contents:
             print(f"- {item}")
     ```

   - **Run `reloads.py`** again. It should reflect the changes made to `filechanges.py` and list the directory contents with updated formatting.

### Example Output

1. **First Run**:
   - `reloads.py` will output:
     ```
     Contents of directory: ['text1.txt', 'text2.txt', 'text3.txt']
     ```

2. **After Removing a File (`text3.txt`) and Running Again**:
   - The output will be updated:
     ```
     Contents of directory: ['text1.txt', 'text2.txt']
     ```

3. **After Updating `filechanges.py`**:
   - If `filechanges.py` is updated to print each file on a new line, running `reloads.py` will show:
     ```
     Updated directory contents:
     - text1.txt
     - text2.txt
     ```

This example demonstrates how to use the `reload` function to dynamically update the behavior of your program based on changes made to imported modules.

## Module Use-cases

### Notes on "Module Use-cases" Text

#### Modules, Packages, and Libraries
- **Modules**: 
  - Represented as single files in Python.
  - Contain Python code: functions, classes, and data members.
  - Example: `math.py`.

- **Packages**:
  - Act as directories that contain multiple modules and sub-packages.
  - Identified by a `__path__` definition.
  - Can have sub-packages, which are directories inside the package directory.
  - Example: `numpy` package, which contains modules like `numpy.linalg`.

- **Libraries**:
  - A broader term that refers to a collection of related packages.
  - Often used interchangeably with packages but generally includes multiple packages.
  - Example: `scikit-learn` is a library that includes packages for machine learning.

#### Installing Packages
- **Python Package Index (PyPI)**:
  - Repository for third-party packages.
  
- **pip**:
  - Package installer for Python.
  - Comes installed by default with Python.
  - Commands:
    - **Mac**: `pip install package_name`
    - **Windows**: `pip install package_name`
  
- **Terminal/Command Line**:
  - Use terminal on Mac or command line interface on Windows.
  - Ensure the Python interpreter used is consistent with the IDE.

- **Verification**:
  - Check pip installation with:
    - **Mac**: `pip --version`
    - **Windows**: `pip --version`
  
#### Using Installed Packages
- After installation, packages are accessible in Python code.
- One-time installation, remains until uninstalled.
  
#### Documentation and Examples
- Check documentation for understanding package functionalities.
- Resources:
  - **Python Package Index (pypi)**: For package documentation.
  - **GitHub**: For open-source packages.
  - **Package websites**: For additional details.

#### Sub-packages
- Packages can contain sub-packages (directories within a package).
- Accessed using dot-notation (e.g., `package.subpackage`).
- Example: In `matplotlib`, sub-package `pyplot` is commonly used.
  
- **Importing Sub-packages**:
  - Example: `import matplotlib.pyplot as plt`
  - Alias (e.g., `plt`) is used for convenience, but other names can be chosen.

#### Practical Tip
- Explore package directory structures by checking module indexes or documentation provided by the package maintainers.

These notes provide a concise overview of how to understand and work with modules, packages, and libraries in Python, including how to install and use them effectively.

Sure! Here’s a practical example to illustrate the concepts of modules, packages, and sub-packages:

### Example

#### 1. **Modules**

Let's say you have a simple module named `calculator.py`:

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

You can use this module in another script as follows:

```python
# main.py
import calculator

result1 = calculator.add(5, 3)
result2 = calculator.subtract(10, 4)

print(f"Addition: {result1}")
print(f"Subtraction: {result2}")
```

#### 2. **Packages**

Suppose you create a package named `math_tools` with the following structure:

```
math_tools/
    __init__.py
    arithmetic.py
    geometry.py
```

- **`__init__.py`**: This file can be empty or used to initialize the package.
- **`arithmetic.py`**: Contains arithmetic functions.
- **`geometry.py`**: Contains geometry-related functions.

**Example of `arithmetic.py`:**

```python
# arithmetic.py
def multiply(a, b):
    return a * b
```

**Example of `geometry.py`:**

```python
# geometry.py
def area_of_circle(radius):
    import math
    return math.pi * (radius ** 2)
```

You can use this package in a script like this:

```python
# main.py
from math_tools import arithmetic, geometry

product = arithmetic.multiply(4, 5)
area = geometry.area_of_circle(7)

print(f"Product: {product}")
print(f"Area of circle: {area}")
```

#### 3. **Sub-packages**

Suppose `math_tools` package has a sub-package named `advanced` with the following structure:

```
math_tools/
    __init__.py
    arithmetic.py
    geometry.py
    advanced/
        __init__.py
        algebra.py
```

- **`advanced/algebra.py`**: Contains algebraic functions.

**Example of `algebra.py`:**

```python
# algebra.py
def quadratic_formula(a, b, c):
    import math
    discriminant = (b ** 2) - (4 * a * c)
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2
```

You can access this sub-package as follows:

```python
# main.py
from math_tools.advanced import algebra

roots = algebra.quadratic_formula(1, -3, 2)

print(f"Roots of the quadratic equation: {roots}")
```

### Summary
- **Module**: A single file (e.g., `calculator.py`).
- **Package**: A directory with modules (e.g., `math_tools`).
- **Sub-package**: A subdirectory within a package (e.g., `math_tools/advanced`).

This example shows how to define and use modules, packages, and sub-packages in Python, illustrating their structure and how to import and use their contents.

## Knowledge check: Modules

## Additional resources
