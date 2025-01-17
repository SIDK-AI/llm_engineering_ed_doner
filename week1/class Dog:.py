class Dog:
    
    # class with a name and age as attributes
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        # method of the class
    def bark(self):
        return f"{self.name} is barking"
        
        
    # create an object from the class
    
my_dog = Dog("Renee",2)
    
print(my_dog.name)
print(my_dog.age)
print(my_dog.bark())