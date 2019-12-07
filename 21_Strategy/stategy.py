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