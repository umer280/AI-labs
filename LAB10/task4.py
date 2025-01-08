#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Employee:
    # Class variable to keep track of the number of employees
    empCount = 0

    # Constructor to initialize employee details
    def __init__(self, empName, salary):
        self.empName = empName
        self.salary = salary
        Employee.empCount += 1  # Increment the employee count

    # Function to display the total number of employees
    def displayCount(self):
        print(f"Total number of employees: {Employee.empCount}")

    # Function to display employee details
    def displayEmployee(self):
        print(f"Employee Name: {self.empName}, Salary: {self.salary}")

# Create instances of Employee
emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 60000)

# Display employee details and count
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()class Employee:
    # Class variable to keep track of the number of employees
    empCount = 0

    # Constructor to initialize employee details
    def __init__(self, empName, salary):
        self.empName = empName
        self.salary = salary
        Employee.empCount += 1  # Increment the employee count

    # Function to display the total number of employees
    def displayCount(self):
        print(f"Total number of employees: {Employee.empCount}")

    # Function to display employee details
    def displayEmployee(self):
        print(f"Employee Name: {self.empName}, Salary: {self.salary}")

# Create instances of Employee
emp1 = Employee("John Doe", 50000)
emp2 = Employee("Jane Smith", 60000)

# Display employee details and count
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()

