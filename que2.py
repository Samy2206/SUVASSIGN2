# Define two classes Dog and Cat, both inheriting from a class Animal that has a method speak(). 
# Override the speak() method in both classes so that Dog says "Woof" and Cat says "Meow". 
# Demonstrate the use of polymorphism by calling the speak() method on instances of both 
# classes.

class Animal:
    def pClass(self):
        print("Animal is parent class")

    def speak(self):
        print("Makes Sound")

class Cat(Animal):
    def speak(self):
        print("Meow")
    
class Dog(Animal):
    def speak(self):
        print("Woof")

cat = Cat()
cat.pClass()
cat.speak()

dog=Dog()
dog.pClass()
dog.speak()