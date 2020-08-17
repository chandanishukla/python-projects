class A:
    pass
e1=A()# it will print nothing because methods are not defined


from abc import *
class A:
    @abstractmethod #it will give error because python dosent support abstract methd in order to use we need to define
    def dispay(self):#abc module
        pass
e=A() # this is abstract class because here only declaration part is there we are not  assigning anything



class A:
    @abstractmethod
    def display(self):
        print("Hiii Python")
e=A()
e.display() #o/p....Hii Python




class A(ABC):
    @abstractmethod
    def display(self):
        pass
class B:
    pass
e=A()#we can not create object for the abc inherited module class
e.display()



class Animal(ABC):
    @abstractmethod
    def display(self):
        pass
class Dog(Animal):
        pass
e=Dog()
e.display()#error we need to define one method inside the dog class



class Animal(ABC):
    @abstractmethod
    def assign(self):
        pass
class Dog(Animal):
    def assign(self):
        print('hello')
e=Dog()
e.display()



class Shape(ABC):
   @abstractmethod
   def area(self):
      pass
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
r = Rectangle(10,20)
print ('area: ',r.area())



class Add(ABC):
    def display(self):
        pass
class Var(Add):
    def display(self):
        self.x=10
        self._y=20
        self.__z=30
    def print(self):
        print("print x",self.x)
        print("print y",self._y)
        print("print z",self.__z)
e=Var()
e.display()
e.print()


class Employee:# public
    def __init__(self, name, sal):
        self.name=name
        self.salary=sal
    def display(self):
        print(self.name)
        print(self.salary)
e=Employee("Kiran",10000,)
e.display()
print(e.salary) #public ..we are calling salary outside the class



class Employee:# protected
    def __init__(self,age,mark):
        self._age=age
        self._mark=mark
    def display(self):
        print(self._age)
        print(self._mark)
e1=Employee(34,95)
e1.display()
print(e1.mark)#we can access protected member outside the class also



class Employee:# private
    def __init__(self,age,mark):
        self.__age = age
        self.__mark = mark

    def display(self):
        print(self.__age)
        print(self.__mark)

e1 = Employee(34, 95)
e1.display()
#print(e1.mark)#we can not access private method outside the class
print(e1._Employee__mark) #we can access private method using this code














