

#class creation,instance variable,static variable
class Student: #class creation
    college_name="VITS" #static variable
    college_number=9977564320
    def display(self):# instance method
        print("the college name is : ",Student.college_name)
        print("the college_number is : ",Student.college_number)

e1=Student() #object creation #e1 is the object reference
e1.display()# method calling by using object reference



class Employee: #class name
    company_name="HAPPY COMPANY " #static variable
    def empinfo(self):
        self.eid=101 #instance variable
        self.ename="venkat"
        self.esalary=300000
    def display(self):
        print("The Company name is : ",Employee.company_name)
        print("Employee id is : ",self.eid)
        print("Employee name is :",self.ename)
        print("Employee salary is : ",self.esalary)
e1=Employee()
e1.empinfo()
e1.display()

# different way of static variable creations
class Employee:
    def add(self):
        Employee.company_name="ABCD" ##static variable inside the class
        self.eid=101
        self.ename='chandani'
    def display(self):
        print(Employee.company_name)
        print(self.eid)
        print(self.ename)
e1=Employee()
e1.add()
e1.display()


class Employee:
    def __init__(self):
        Employee.company_name='ABC' #static variable inside constructor
        self.eid=10
        self.ename='chandani'
    def display(self):
        print(Employee.company_name)
        print(self.eid)
        print(self.ename)
e1=Employee()
e1.display()
#

class Employee: # constructor with parameter
    cname="ABC"
    phone=8960430505
    def __init__(self,eid,ename,esal):
        self.empid=eid
        self.ename=ename
        self.esal=esal
    def display(self):
        print(Employee.cname)
        print(Employee.phone)
        print(self.empid)
        print(self.ename)
        print(self.esal)
e1=Employee(101,'chandani',21356)
e1.display()