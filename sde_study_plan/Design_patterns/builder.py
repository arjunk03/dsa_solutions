
import time
from enum import Enum
PizzaProgress = Enum("PizzaProgress", "queued preparation baking ready")
PizzaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum("PizzaTopping","mozzarella double_mozzarella bacon ham mushrooms red_onion oregano",
)
# Delay in seconds
STEP_DELAY = 3

print(dir(PizzaProgress))

class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
    
    def __str__(self):
        return self.name
    
    def prepare_dough(self, dough):
        self.dough = dough
        print(f"preparing the {self.dough.name} dough of your {self}...")
        time.sleep(STEP_DELAY)
        print(f"done with the {self.dough.name} dough")

class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza("margarita")
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza("creamy bacon")
        self.progress = PizzaProgress.queued
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (
            builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake,
        )
        [step() for step in steps]
    
    @property
    def pizza(self):
        return self.builder.pizza

def validate_style(builders):
    try:
        input_msg = "What pizza would you like, [m]argarita or [c]reamy bacon? "
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = "Sorry, only margarita (key m) and creamy bacon (key c) are available"
        print(error_msg)
        return (False, None)
    return (True, builder)

def main():
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f"Enjoy your {pizza}!")

main()