"""

Simple example on Class and object
# Class is blueprint for the list of instances (Objects)
# In python, self is the object pass thought
# __init__ is like constructor in JAVA

"""


class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f'{first_name}.{last_name}@company.co.uk'

    def full_name(self):
        return f'Full name is : {self.first_name} {self.last_name}'


emp1 = Employee('Egambaram', 'Panneerselvam', 65000)
emp2 = Employee('Test', 'User', 50000)

print(emp1.email)
print(emp1.full_name())

print(emp2.email)
print(emp2.full_name())

