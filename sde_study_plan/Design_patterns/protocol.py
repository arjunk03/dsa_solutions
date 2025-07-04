from typing import Protocol, runtime_checkable

@runtime_checkable
class Flyer(Protocol):
    def fly(self) -> None:
        """Method to make the object fly."""
        pass

class Bird:
    def fly(self) -> None:
        print("Bird is flying")

class Airplane:
    def fly(self) -> None:
        print("Airplane is flying") 

class Helicopter:
    def flya(self) -> None:
        print("Helicopter is flying")


def print_flyer(flyer: Flyer) -> None:
    """Function that accepts any object that implements the Flyer protocol."""
    flyer.fly()

if __name__ == "__main__":
    bird = Bird()
    airplane = Airplane()
    helicopter = Helicopter()

    print_flyer(bird)      # Output: Bird is flying
    print_flyer(airplane)  # Output: Airplane is flying
    # print_flyer(helicopter)  # Output: Helicopter is flying

    print(isinstance(bird, Flyer))      # Output: True
    print(isinstance(airplane, Flyer))  # Output: True
    print(isinstance(helicopter, Flyer))  # Output: False (since Helic