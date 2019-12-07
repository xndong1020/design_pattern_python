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

  # shape2 = ColoredShape(
  #   shape,
  #   'Red'
  # ) # Exception: Cannot apply same decorator twice
  