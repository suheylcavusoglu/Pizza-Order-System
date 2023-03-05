

class Pizza:
    def __init__(self):
        self.description = "Unknown Pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

    # Defined the pizza superclass with get_description() and get_cost() methods.


class ClassicPizza(Pizza):
    def __init__(self):
        self.description = "Classic Pizza"
        self.cost = 109.90


class MargheritaPizza(Pizza):
    def __init__(self):
        self.description = "Margherita Pizza"
        self.cost = 129.90


class TurkPizza(Pizza):
    def __init__(self):
        self.description = "Turk Pizza"
        self.cost = 139.90


class PlainPizza(Pizza):
    def __init__(self):
        self.description = "Plain Pizza"
        self.cost = 99.90

# Defined the pizza subclasses with their own description and cost variables.


class Decorator(Pizza):
    def __init__(self, pizza):
        self.component = pizza

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)

# Defined the Decorator superclass with get_description() and get_cost() methods.


class Olives(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Olives"
        self.cost = 3.90


class Mushrooms(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Mushrooms"
        self.cost = 4.90


class GoatCheese(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Goat Cheese"
        self.cost = 7.90


class Meat(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Meat"
        self.cost = 9.90


class Onions(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Onions"
        self.cost = 2.90


class Corn(Decorator):
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)
        self.description = "Corn"
        self.cost = 5.90

# Defined the sauce classes with their own description and cost variables.
