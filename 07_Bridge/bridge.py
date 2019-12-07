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