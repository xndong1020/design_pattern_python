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


john = EmployeeFactory.new_sydney_employee("John")
jane = EmployeeFactory.new_melbourne_employee("Jane")
print(john)
print(jane)