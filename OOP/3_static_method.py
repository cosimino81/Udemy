class Employee:
  
  def employeeDetails(self):
    self.name = "Mary"
    age = 30
    print "My name is", self.name
    print "My age is", age
    print " "
  # The decorator ignore the bounding of the object
  @staticmethod
  def printDetails():
    # This give an error without the @staticmethod
    print "My name is pippo!"

employee = Employee()

employee.employeeDetails()

employee.printDetails()
