from abc import ABC, abstractmethod

# 1. Component Interface
class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass

# 2. Concrete Component
class SimpleCoffee(Coffee):
    def get_cost(self):
        return 5
    
    def get_description(self):
        return "Simple Coffee"

# 3. Decorator Base Class
class CoffeeDecorator(Coffee, ABC):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee
    
    @abstractmethod
    def get_cost(self):
        pass
    
    @abstractmethod
    def get_description(self):
        pass

# 4. Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def __init__(self, decorated_coffee):
        super().__init__(decorated_coffee)
    
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 2
    
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Milk"

class SugarDecorator(CoffeeDecorator):
    def __init__(self, decorated_coffee):
        super().__init__(decorated_coffee)
    
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 1
    
    def get_description(self):
        return self.decorated_coffee.get_description() + ", Sugar"

# The Client
if __name__ == "__main__":
    # Create a simple coffee
    my_coffee = SimpleCoffee()
    print(f"Description: {my_coffee.get_description()}, Cost: ${my_coffee.get_cost()}") # Simple Coffee, Cost: $5

    # Decorate it with milk
    my_coffee = MilkDecorator(my_coffee)
    print(f"Description: {my_coffee.get_description()}, Cost: ${my_coffee.get_cost()}") # Simple Coffee, Milk, Cost: $7

    # Decorate it with sugar
    my_coffee = SugarDecorator(my_coffee)
    print(f"Description: {my_coffee.get_description()}, Cost: ${my_coffee.get_cost()}") # Simple Coffee, Milk, Sugar, Cost: $8