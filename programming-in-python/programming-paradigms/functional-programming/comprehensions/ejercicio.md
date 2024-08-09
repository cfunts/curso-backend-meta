Here’s how you can implement the functions as described:

### Step 1: Implement the `to_mod_list()` Function
This function will use the `map()` function to apply the `mod()` function to each element in the `employee_list` and return the result as a list.

```python
def to_mod_list(employee_list, mod):
    # Apply mod() to each element in employee_list using map()
    map_emp = map(mod, employee_list)
    # Convert the map object to a list and return it
    return list(map_emp)
```

### Step 2: Implement the `generate_usernames()` Function
This function will use list comprehension to replace spaces in each string of the modified list with underscores.

```python
def generate_usernames(mod_list):
    # Use list comprehension to replace spaces with underscores
    return [item.replace(" ", "_") for item in mod_list]
```

### Step 3: Implement the `map_id_to_initial()` Function
This function will create a dictionary where the keys are the first initials of employee names and the values are their corresponding IDs.

```python
def map_id_to_initial(employee_list):
    # Use dictionary comprehension to map first initials to employee IDs
    return {employee['name'][0]: employee['id'] for employee in employee_list}
```

### Example Usage
Assuming you have the `employee_list` and a `mod()` function defined, your script might look like this:

```python
# Example employee data and mod function
employee_list = [
    {"name": "Lisa", "department": "Cold Storage", "id": 101},
    {"name": "John", "department": "Inventory", "id": 102},
    {"name": "Kate", "department": "Logistics", "id": 103},
]

def mod(employee):
    return f"{employee['name']}_{employee['department']}"

# Step 1: Modify the employee list
mod_list = to_mod_list(employee_list, mod)

# Step 2: Generate usernames
usernames = generate_usernames(mod_list)
print("Usernames:", usernames)

# Step 3: Map IDs to initials
id_initial_map = map_id_to_initial(employee_list)
print("ID to Initial Map:", id_initial_map)
```

### Running the Script
To run the script, you would open your terminal and execute:

```bash
python3 comprehensions.py
```

This will produce the desired output based on your employee data and the functions you've implemented.