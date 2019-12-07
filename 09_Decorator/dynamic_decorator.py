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