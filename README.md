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

### Section 6: Adapter

1. Determine the API that you have, and the API you need
2. Create an Adapter component, which aggregates (has a reference to) the adaptee

```py
from abc import ABC

class Target(ABC):
    """
    The Target defines the domain-specific interface required by the client code.
    """

    def request(self) -> str: pass


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """
    The client code supports all concrete classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface, which doesn't work well with my code")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)

```

### Section 7: Bridge

1. Decouple abstraction from implementation
2. Both can exist as hierarchies, both can change without affecting each other

```py
# line type: solid, dashed
# color: colored, black & white
# shape: circle, square

from abc import ABC

class Formatter(ABC):
  def format_circle(self, str): pass
  def format_square(self, str): pass

class DashedFormatter(Formatter):
  def format_circle(self, str):
    print(f'Use dashed line to circle')
  def format_square(self, str):
    print(f'Use dashed line to square')

class SolidFormatter(Formatter):
  def format_circle(self, radius):
    print(f'Use solid line to circle')
  def format_square(self, side):
    print(f'Use solid line to square')

class Renderer(ABC):
  def render_circle(self, radius): pass
  def render_square(self, side): pass

class ColoredRenderer(Renderer):
  def render_circle(self, radius):
    print(f'Coloring a circle with radius {radius}')
  def render_square(self, side):
    print(f'Coloring a square with side {side}')

class BlackAndWhiteRenderer(Renderer):
  def render_circle(self, radius):
    print(f'Drawing a circle with radius {radius}')
  def render_square(self, side):
    print(f'Drawing a square with side {side}')

class Shape:
  """
  Base class for all subtypes of shapes
  """
  def __init__(self, renderer: Renderer, formatter: Formatter):
    self.renderer = renderer
    self.formatter = formatter

  def draw(self): pass

class Circle(Shape):
  def __init__(self, renderer: Renderer, formatter: Formatter, radius):
    super().__init__(renderer, formatter)
    self.radius = radius

  def draw(self):
    self.formatter.format_circle(self.renderer.render_circle(self.radius))

class Square(Shape):
  def __init__(self, renderer: Renderer, formatter: Formatter, side):
    super().__init__(renderer, formatter)
    self.side = side

  def draw(self):
    self.formatter.format_square(self.renderer.render_square(self.side))

if __name__ == '__main__':
  square_black_white = Square(BlackAndWhiteRenderer(), DashedFormatter(), 10)
  square_black_white.draw()
  # Drawing a square with side 10
  # Use dashed line to square

  circle_colored = Circle(ColoredRenderer(), SolidFormatter(), 5)
  circle_colored.draw()
  # Coloring a circle with radius 5
  # Use solid line to circle
```

### Section 09: Decorator

1. Python's functional decorators wrap functions, no direct relations to the GoF Decorator pattern
2. A decorator keeps the reference to the decorated object(s)
3. Adds utility attributes and methods to augment the object's feature
4. Proxying of underlying calls can be done dynamically (dynamic decorator)
5. May or may not forward calls to the underlying object (dynamic decorator)

Functional decorator ( no direct relations to the GoF Decorator pattern )

```python
import time


def time_it(func):
  def wrapper():
    start = time.time()
    result = func()
    end = time.time()
    print(f"{func.__name__} took {int((end-start)*1000)} ms")
    return result
  return wrapper

@time_it
def some_op():
  print('Start op')
  time.sleep(1)
  print('Done op')
  return 123

if __name__ == "__main__":
  some_op()
```

Class Decorator (keeps the reference to the decorated object(s) via **init**)

```python
from abc import ABC

class Shape(ABC):
  def __str__(self):
    return ''


class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def resize(self, factor):
    self.radius *= factor

  def __str__(self):
    return f"A circle of radius {self.radius}"

class Square(Shape):
  def __init__(self, side):
    self.side = side

  def __str__(self):
    return f"A square of radius {self.side}"


class ColoredShape(Shape):
  def __init__(self, shape, color):
    # prevent use same decorator twice on same underlying class
    if isinstance(shape, ColoredShape):
      raise Exception("Cannot apply same decorator twice")

    self.shape = shape # always hold a reference to the underlying class
    self.color = color

  def __str__(self):
    return f"{self.shape} of color {self.color}"


if __name__ == "__main__":
  shape = ColoredShape(
    Circle(100),
    'Red'
  )
  print(shape) # A circle of radius 100 of color Red
```

Dynamic Decorator (Proxying of underlying calls can be done dynamically, by forward calls to the underlying object)
For example: in below code, use `__getattr__` magic method to forward calls to the underlying file object

```python
from io import TextIOWrapper

class FileWithLogging:
  def __init__(self, file: TextIOWrapper):
    self.file = file

  def writelines(self, strings):
    self.file.writelines(strings)
    print(f'wrote {len(strings)} lines')

  """
  Below we override getattr, setattr, and delattr method of FileWithLogging class,
  to redirect IO operation to self.file
  """

  # Python will call this method whenever you request an attribute that hasn't already been defined.
  # But if the attribute does exist, __getattr__ won’t be invoked
  def __getattr__(self, item):
    print(f'__getattr__ invoked with item: {item}')
    return getattr(self.__dict__['file'], item) # get file[item], eg: file.write, file.close

  # Called when an attribute assignment is attempted
  def __setattr__(self, key, value):
    # print(f'__setattr__ invoked with key: {key}, value: {value}')
    if key == 'file':
      """
      If __setattr__() wants to assign to an instance attribute,
      it should not simply execute self.name = value
      this would cause a recursive call to itself.
      Instead, it should insert the value in the dictionary of instance attributes,
      e.g., self.__dict__[name] = value
      """
      self.__dict__[key] = value
    else:
      setattr(self.__dict__['file'], key)

  # Called when an attribute deletion is attempted.
  def __delattr__(self, item):
    delattr(self.__dict__['file'], item)

  def __iter__(self):
    return self.file.__iter__()

  def __next__(self):
    return self.file.__next__()


if __name__ == "__main__":
  file = open("./hello.txt", "w")

  file_with_logging = FileWithLogging(file)

  file_with_logging.writelines([
    "First line\n",
    "Second line\n",
    "Third line\n"
  ])

  file_with_logging.write('testing last line.')
  file_with_logging.close()
```

### Section 12: Proxy

1. A proxy has the same interface as the underlying object
2. To create a proxy, simply replicate the existing interface of an object
3. Add relevant functionality to the redefined member function

Protection proxy

```python
class ProtectedResource:
    def __init__(self, user):
        self.user = user

    def secured_method(self):
        print(self.user.name)


class User:
    def __init__(self, name, auth_code):
        self.name = name
        self.auth_code = auth_code


class ProtectedResourceProxy:
    def __init__(self, user):
        self.user = user

    def secured_method(self):
        if self.user.auth_code != "my super secret auth code":
            print("Invalid auth code")
            return

        print(self.user.name)


if __name__ == "__main__":
    user = User("Jeremy", "my super secret auth code")

    # Instead of calling ProtectedResource directly,
    # now we call its proxy, which has added security logic
    # resource = ProtectedResource(user)
    resource = ProtectedResourceProxy(user)
    resource.secured_method()
```

Virtual Proxy (Lazy)

```python
class Bitmap:
    def __init__(self, filename):
        print("Bitmap initialized")
        self.filename = filename

    def draw(self):
        print(f"Start drawing bitmap loaded from {self.filename}")


class LazyBitmapProxy:
    def __init__(self, filename):
        self.filename = filename
        self._instance = None

    def draw(self):
        if self._instance is None:
            self._instance = Bitmap(self.filename)
        print(f"Start drawing bitmap loaded from {self.filename}")


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


if __name__ == "__main__":
    bmp = LazyBitmapProxy("emoji.png")
    draw_image(bmp)

```

### Section 13: Chain of Responsibility

```py
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
```

### Section 21: Strategy

1. Define an algorithm at high level
2. Define the interface you expect each concrete strategy to follow
3. Provide for dynamic composition of strategies in the resulting object

```python
from abc import ABC

class FormatStrategy(ABC):
  def start(self, buffer): pass
  def text(self, buffer, item): pass
  def end(self, buffer): pass


class MarkdownStrategy(FormatStrategy):
  def text(self, buffer, item):
    [ buffer.append(f' * {i}\n') for i in item ]

class HtmlStrategy(FormatStrategy):
  def start(self, buffer):
    buffer.append('<ul>\n')

  def text(self, buffer, item):
    [ buffer.append(f'  <li>{i}</li>\n') for i in item ]

  def end(self, buffer):
    buffer.append('</ul>')


class TextProcessor:
  def __init__(self, formatStrategy:FormatStrategy = MarkdownStrategy()):
    self.buffer = []
    self.formatStrategy = formatStrategy

  def process(self, items: list):
    self.formatStrategy.start(self.buffer)
    self.formatStrategy.text(self.buffer, items)
    self.formatStrategy.end(self.buffer)

  def __str__(self):
    return ''.join(self.buffer)

if __name__ == '__main__':
  # textProcessor = TextProcessor()
  textProcessor = TextProcessor(HtmlStrategy())
  items = [
    "First item",
    "Second item",
    "Third item"
  ]
  textProcessor.process(items)
  print(textProcessor)
```
