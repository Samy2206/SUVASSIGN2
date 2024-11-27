# Create two classes Person and Employee, where Person has attributes name and age, and 
# Employee has an attribute employee_id. Create a class Manager that inherits from both Person 
# and Employee. Write a method to display the manager’s details.


#WAY 1
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def display(self):
#         print(f"Details of person\nName: {self.name} and age: {self.age}")
# class Employee:
#     def __init__(self,employee_id):
#         self.employee_id=employee_id
    
#     def display(self):
#         print(f"Employee id of employee is:{self.employee_id}")

# class Manager(Person,Employee):
#     def __init__(self,name,age,employee_id):
#         Person.__init__(self,name,age)
#         Employee.__init__(self,employee_id)
    
#     def display(self):
#         print("Details of Manager:\n")
#         print(f"Name:{self.name}\nAge:{self.age}\nEmployee Id:{self.employee_id}")
    
# man = Manager("Sam",21,1001)
# man.display()


class Person:
    def getPersonDetails(self):
        self.name=input("Enter name of person:")
        self.age=int(input("Enter Age of the person: "))
    
    def display(self):
        print(f"Details of person\nName: {self.name} and age: {self.age}")
    
class Employee:
    def getEmployeeDetails(self):
        self.employee_id=int(input("Enter the employee id: "))
    
    def display(self):
        print(f"Employee id of employee is:{self.employee_id}")

#WAY2
# class Manager(Person,Employee):
#     def display(self):
#         print(f"Name:{self.name}\nAge:{self.age}\nEmployee Id:{self.employee_id}")


#WAY3
class Manager(Person,Employee):
    def __init__(self):
        Person.getPersonDetails(self)
        Employee.getEmployeeDetails(self)
    
    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}\nEmployee Id:{self.employee_id}")
    
manager=Manager()
# manager.getPersonDetails()
# manager.getEmployeeDetails()
manager.display()