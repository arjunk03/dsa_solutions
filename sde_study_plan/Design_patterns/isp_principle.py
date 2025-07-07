from abc import ABC, abstractmethod

class Printer:
    @abstractmethod
    def print(self, message: str) -> None:
        print(message)

class ConsolePrinter(Printer):
    def scan(self, message: str) -> None:
        print(f"Console: {message}")


pr = ConsolePrinter()
pr.print("Hello, World!")

a = 260
b = 260
print(id(a))
print(id(b))  # True, because small integers are cached in Python