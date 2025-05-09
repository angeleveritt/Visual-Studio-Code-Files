# ## Exercise 1: **Access and Update a Nested Dictionary**
#Requirements:
# Create a nested dictionary representing a company's employees. Each key should be an employee ID, and the value should be another dictionary containing "name", "age", and "position".
# Access and print the position of a specific employee based on their ID.
# Update the age of one employee and print the updated dictionary.


employees = {
    "employee_id":{"name": "Employee Name", "age": None, "position": "None"}}
print(employees)
print(employees."employee_id")


"""for field_name, value in employees.items():
    employees[field_name]["value"] = input(employees[field_name]["name"] + ":")

print(employees)

def get_input():
    employees = {                                                              # nested dictionary version
        "customer_name": {"name": "Customer name", "value": None},
        "weight_kg": {"name": "Package weight (kg)", "value": None},                # how do I add the Int here // changed from None to 0 to get integer but the input from user still text
        "cubic_meters": {"name": "Package volume (cubic meters)", "value": None},   # how do I add the Int here // changed from None to 0 to get integer but the input from user still text
        "dangerous": {"name": "Dangerous goods? (y/n)", "value": None}  }"""


