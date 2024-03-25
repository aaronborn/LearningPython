class ParentClass:
    def __init__(self):
        self.parent_attribute = "I am from the parent class"

    def parent_method(self):
        print("This is a method from the parent class")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.child_attribute = "I am from the child class"

    def child_method(self):
        print("This is a method from the child class")

# Creating an instance of the ChildClass
child = ChildClass()

# Accessing attributes and methods from both the parent and child classes
print(child.parent_attribute)
child.parent_method()
print(child.child_attribute)
child.child_method()
