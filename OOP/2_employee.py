# Create a class 
# The following class contain two methods and three variable
class Person:
  title = "Hello world"
  
  def __init__(self, name, last_name, age):
    self.name = name
    self.last_name = last_name
    self.age = age
    
  def myfunct(self):
    print "Hello, my name is " + self.name + " and I'm " + str(self.age)
    
  def changeName(self, new_name):
    self.name = new_name




# Instancing a class    
employee = Person("Peter", "Gomez", 33)

print employee.title + "\n"
print employee.last_name + "\n"
print employee.myfunct()
print " "

# Instancing a new attribute inside the class (from the object)
employee.subtitle = "The world is yours!"
print employee.subtitle + "\n"

# Modify and Object inside the class (without method 1)
employee.name = "Pippo"
print employee.name + "\n"

# Modify and Object inside the class (without method 2)
Person.title = "Hello Jungle"
print employee.title + "\n"

# Modify and Object inside the class (using method)
employee.changeName("Kulibali")
print employee.name 

# Deleting an Object Properties
del employee.age
print employee.age

# Deleting Object
del p1
print p1.name
