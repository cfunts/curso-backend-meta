# Step 1: Open the comprehensions.py file OK

#Step 2: Implement the to_mod_list() function by using the 
# map() function to apply mod() to all elements within employee_list.

#Assign the result of it to a new variable called map_emp. 
# Convert map_emp to a list and return it. OK

   #The mod() function returns a string value for example such as “Lisa_Cold Storage” 
   # from the dictionary passed to it. 

# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
   """ Modifies the employee list of dictionaries into list of employee-department strings

   [IMPLEMENT ME] 
      1. Use the map() method to apply mod() to all elements in employee_list

   Args:
      employee_list: list of employee objects

   Returns:
      list - A list of strings consisting of name + department.
   """
   ### WRITE SOLUTION CODE HERE

   # Apply mod() to each element in employee_list using map()
   map_emp = map(mod, employee_list)
   #Convert the map object to a list and return it
   return list(map_emp)

   raise NotImplementedError()

def generate_usernames(mod_list):
   """ Generates a list of usernames 

   [IMPLEMENT ME] 
      1. Use list comprehension and the replace() function to replace space
         characters with underscores

      List comprehension looks like:
      list = [ function() for <item> in <list> ]

      The format for the replace() function is:

      test_str.replace(“a”, “z”) # replaces every “a” in test_str with “z”

   Args:
      mod_list: list of employee-department strings

   Returns:
      list - A list of usernames consisting of name + department delimited by underscores.
   """
   ### WRITE SOLUTION CODE HERE
   return [x.replace(" ", "_") for x in mod_list]

   raise NotImplementedError()

def map_id_to_initial(employee_list):
   """ Maps employee id to first initial

   [IMPLEMENT ME] 
      1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

      Dictionary comprehension looks like:
      dict = { key : value for <item> in <list> }

   Args:
      employee_list: list of employee objects

   Returns:
      dict - A dictionary mapping an employee's id (value) to their first initial (key).
   """
   ### WRITE SOLUTION CODE HERE
   return {employee['name'][0]: employee['id'] for employee in employee_list}

   raise NotImplementedError()

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")#Modified employee list: ['John_Kitchen', 'Paul_House Floor', 'Sarah_Management', 'Lisa_Cold Storage', 'Ryan_Inventory Mgmt', 'Gill_Cashier']

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n") #List of usernames: ['John_Kitchen', 'Paul_House_Floor', 'Sarah_Management', 'Lisa_Cold_Storage', 'Ryan_Inventory_Mgmt', 'Gill_Cashier']

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")#Initials and ids: {'J': 12345, 'P': 12456, 'S': 12478, 'L': 12434, 'R': 12483, 'G': 12419}

if __name__ == "__main__":
   main()