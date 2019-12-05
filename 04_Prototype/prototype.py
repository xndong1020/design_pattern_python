import copy

class Address:
  def __init__(self, suite, street_address, city):
    self.street_address = street_address
    self.suite = suite
    self.city = city
  
  def __str__(self):
    return f"{self.suite}, {self.street_address}, {self.city}"

class Person:
  def __init__(self, name, address):
    self.name = name
    self.address = address

  def __str__(self):
    return  f"{self.name} lives @ {self.address}"

# create prototype
john = Person("John", Address('301', 'London Road', "Sydney"))
print(john)
# deep copy from prototype
jane = copy.deepcopy(john)
# then customize it 
jane.name = 'Jane'
jane.address = copy.deepcopy(john.address)
jane.address.suite = '302'
jane.address.city = 'Melbourne'
print(jane)