from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size   
        pass

class ProductFilter:
    @staticmethod
    def filter_by_color(products, color):
        return [p for p in products if p.color == color]

    @staticmethod
    def filter_by_size(products, size):
        return [p for p in products if p.size == size]

    @staticmethod
    def filter_by_color_and_size(products, color, size):
        return [p for p in products if p.color == color and p.size == size]


class Specification:
    def is_satisfied(self, item):
        raise NotImplementedError("Must implement is_satisfied method")

    def __and__(self, other):
        return AndSpecification(self, other)
    
    def __or__(self, other):
        return OrSpecification(self, other)
    

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class OrSpecification(Specification):
    def __init__(self, *specifications):
        self.specifications = specifications

    def is_satisfied(self, item):
        return any(spec.is_satisfied(item) for spec in self.specifications)

class AndSpecification(Specification):
    def __init__(self, *specifications):
        self.specifications = specifications

    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.specifications)
    

class BetterFilter:
    @staticmethod
    def filter(products, specification):
        return [p for p in products if specification.is_satisfied(p)]   
    



tv = Product("TV", Color.RED, Size.MEDIUM)
sofa = Product("Sofa", Color.GREEN, Size.LARGE)
table = Product("Table", Color.BLUE, Size.SMALL)
car = Product("Car", Color.RED, Size.LARGE)
bed = Product("Bed", Color.GREEN, Size.MEDIUM)
products = [tv, sofa, table, car, bed]

# Example usage    
filtered_by_color = ProductFilter.filter_by_color(products, Color.RED)
filtered_by_size = ProductFilter.filter_by_size(products, Size.MEDIUM)
filtered_by_color_and_size = ProductFilter.filter_by_color_and_size(products, Color.GREEN, Size.LARGE)
print("Filtered by color (RED):", [p.name for p in filtered_by_color])
print("Filtered by size (MEDIUM):", [p.name for p in filtered_by_size])
print("Filtered by color (GREEN) and size (LARGE):", [p.name for p in filtered_by_color_and_size])


# Using Specification Pattern
color_spec = ColorSpecification(Color.RED)
size_spec = SizeSpecification(Size.MEDIUM)
filtered_by_spec = BetterFilter.filter(products, color_spec & size_spec)
print("Filtered by specification (RED and MEDIUM):", [p.name for p in filtered_by_spec])    
# Using OrSpecification
or_spec = color_spec | size_spec
filtered_by_or_spec = BetterFilter.filter(products, or_spec)
print("Filtered by OrSpecification (RED or MEDIUM):", [p.name for p in          filtered_by_or_spec])
# Using AndSpecification
and_spec = color_spec & size_spec
filtered_by_and_spec = BetterFilter.filter(products, and_spec)
print("Filtered by AndSpecification (RED and MEDIUM):", [p.name for p in filtered_by_and_spec])    
# Using multiple specifications
multi_spec = ColorSpecification(Color.RED) & SizeSpecification(Size.MEDIUM) | SizeSpecification(Size.LARGE)
filtered_by_multi_spec = BetterFilter.filter(products, multi_spec)
print("Filtered by multiple specifications (RED and MEDIUM or LARGE):", [p.name for p in filtered_by_multi_spec])