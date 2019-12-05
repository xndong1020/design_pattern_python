## Design Patterns in Python

### Section 3: Factory

- A `factory method` is a static method that creates objects
- A `factory` is an entity that can take care of object creation
- A `factory` can be an external class, or reside inside the object as an inner class
- Hierarchies(family) of factories can be used to create related object

Factory Class

```python
from math import cos, sin


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x is {str(self.x)}, y is {str(self.y)}"

    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))


if __name__ == "__main__":
    my_point = Point(2, 3)
    my_point_factory = my_point.PointFactory()
    p1 = my_point_factory.new_cartesian_point(my_point.x, my_point.y)
    p2 = my_point_factory.new_polar_point(my_point.x, my_point.y)
```

Abstract Factory

```python
from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    """
    Abstract class for concrete products(drinks)
    """

    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("This is a tea product")


class Coffee(HotDrink):
    def consume(self):
        print("This is a Coffee product")


class HotDrinkFactory(ABC):
    """
    Abstract class for a family of factories
    """

    def produce(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def produce(self, amount=2):
        print(f"{amount} {'cups' if amount > 1 else 'cup'} of Tea has been produced")
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def produce(self, amount=2):
        print(f"{amount} {'cups' if amount > 1 else 'cup'} of Coffee has been produced")
        return Coffee()


class Drinks(Enum):
    TEA = auto()
    COFFEE = auto()


if __name__ == "__main__":
    target_product = "COFFEE"

    if target_product not in Drinks.__members__:
        raise ValueError(f"{target_product} is not supported product type.")

    # capitalize first letter, lower remaining letters
    # eg: 'COFFEE' to 'Coffee'
    product_name = f"{target_product[0]}{target_product[1:].lower()}"

    factory_name = f"{product_name}Factory"

    factory_instance = eval(factory_name)()

    product = factory_instance.produce()

    print("product produced:", type(product))

```

### Section 4： Prototype

1. To implement a prototype, firstly partially/fully construct an object, and store it somewhere (like we did forsyndey_office_emp_proto and melbourne_office_emp_proto)
2. Then you deepcopy the prototype
3. Then customize the deeocopy instance
4. You can then use a factory to provide a convenient API for using prototypes (like the \_\_new_employee method)

```python
import copy

class Address:
  def __init__(self, suite, street_address, city):
    self.street_address = street_address
    self.suite = suite
    self.city = city

  def __str__(self):
    return f"{self.suite}, {self.street_address}, {self.city}"

class Employee:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def __str__(self):
    return  f"{self.name} works @ {self.address}"

class EmployeeFactory:
  # setup 2 prototypes to be used
  syndey_office_emp_proto = Employee('', Address('001', "Main street", "Sydney"))
  melbourne_office_emp_proto = Employee('', Address('500', "Kings street", "Melbourne"))

  @staticmethod
  # Used for deep copy a prototype, then customize it
  def __new_employee(proto, name):
    new_emp = copy.deepcopy(proto)
    new_emp.name = name
    return new_emp

  @staticmethod
  def new_sydney_employee(name):
    return EmployeeFactory.__new_employee(EmployeeFactory.syndey_office_emp_proto, name)

  @staticmethod
  def new_melbourne_employee( name):
    return EmployeeFactory.__new_employee(EmployeeFactory.melbourne_office_emp_proto, name)


john = EmployeeFactory.new_sydney_employee("John") # John works @ 001, Main street, Sydney
jane = EmployeeFactory.new_melbourne_employee("Jane") # Jane works @ 500, Kings street, Melbourne
```
