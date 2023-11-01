# variable scope w.r.t class
# global scope
from builtins import id


class Employee:
    firstName: str = "dhanunjai"
    lastName: str = "sundhar"


emp = Employee()
print(emp.firstName)


# partially private scope

class Employee:
    _firstName: str = "sai"
    lastName: str = "sundhar"


emp = Employee()
print(emp._firstName)


# # variable scope w.r.t functions
# global
def schoolName():
    global fName
    fName = "zilla prashad"
    lName = "high schools"
schoolName()
print(fName)
# print(lName)


# exxample of abstraction
class id:
    __firstName :str = "dhanunjai"
    lastName : str = "sai"
    def dhoni(self):
         return self.__firstName +" "+self.lastName
emp = id()
emp.lastName = "sundhar"
print(emp.dhoni())
