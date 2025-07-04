from abc import ABC, abstractmethod

class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass

class MyClass(MyInterface):
    def my_method(self):
        print("Implementation of my_method in MyClass")

if __name__ == "__main__":
    obj = MyClass()
    obj.my_method()  # Output: Implementation of my_method in MyClass
    # Uncommenting the next line will raise an error because MyInterface cannot be instantiated directly
    # interface_obj = MyInterface()  # Raises TypeError: Can't instantiate abstract class MyInterface with abstract methods my_method