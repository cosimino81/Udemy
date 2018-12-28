
class SocialEmployee:
  
  def employeeDetails(self):
    self.name = "Mary"
    age = 30
    print "My name is", self.name
    print "My age is", age
 
class BankEmployee:
    
    def employeeDetails(self):
        self.code = "CR7"
        team = "Juventus"
        role = "Attack"
        print "The employee code in {} he plays to the {} as {}".format(self.code, team, role)

SocialEmployeeOBJ = SocialEmployee()
BankEmployeeOBJ = BankEmployee()

SocialEmployeeOBJ.employeeDetails()
BankEmployeeOBJ.employeeDetails()
