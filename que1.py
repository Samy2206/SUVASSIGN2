# Write a Python program that defines a class Vehicle with attributes make and model. Create a 
# subclass Car that inherits from Vehicle and adds a new attribute number_of_doors. Implement 
# a method to display details of a car.


class Vehicle:
    def __init__(self,made,model):
        self.made=made
        self.model=model

    def display(self):
        print(f"Car was made in :{self.made} and model is:{self.model}")
    

class Car(Vehicle):
    def __init__(self,made,model,number_of_doors):
        super().__init__(made,model)
        self.number_of_doors=number_of_doors
    
    def display(self):
        print(f"Car Model is {self.model} made in {self.made} and having {self.number_of_doors}")


car = Car(2024,"Toyota",5)
car.display()