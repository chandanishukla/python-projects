class SBI:# single inheritance
    ifsc_code=1919 #static variable
    branch_name='DA10'
    def assign(self): #instance method
        SBI.ifsc_code = 1919
        print("hiii")
class Customer(SBI):
    def __init__(self): #constructor
        SBI.ifsc_code=1919
        self.cid=101 #instance variable
        self.cname="gf"
    def display(self):
        print(SBI.ifsc_code)
        print(SBI.branch_name)
        print(self.cid)
        print(self.cname)
e1=Customer()
e1.assign()
e1.display()


class A: #multilevel inheritance
    def ass(self):
        print("hiii")
class B(A):
    def ss(self):
        print("byeee")
class C(B):
    def fd(self):
        print("dsd")
e=C()
e.ass()
e.fd()
e.ss()




class A: # multiple in
    def D(self):
        print("hdjfh")
class B:
    def c(self):
        print("dfdg")
class C(A,B):
    def s(self):
        print("dfhdj")
e=B()
e.c()
e.s()
e.D()



class Animal:
    def bark(self):
        print("barking")
class Dog(Animal):
    def eat(self):
        print("ffhdj")
class cat(Animal):
    def walk(self):
        print("vbffd")
class cow(Dog):
    def legs(self):
        print("four legs")
# e=cow()
# e.legs()
# e.eat()
# e.bark()
e1=cat()
e1.walk()
e1.bark()


class A:
    def __init__(self,aid,aname,asal):
        self.aid=aid
        self.aname=aname
        self.asal=asal
e=A()  # __init__() missing 3 required positional arguments: 'aid', 'aname', and 'asal'(Type error we need to pass the arguments)


class A:
    def __init__(self,aid,aname,asal):
        self.aid=aid
        self.aname=aname
        self.asal=asal
e=A(101,'chandani',3240034) # the output will be blank because there should be atleat one method to define one method and need to call that method


class A:
    def __init__(self,aid,aname,asal):
        self.aid=aid
        self.aname=aname
        self.asal=asal
    def display(self):
        print(self.aid)
        print(self.aname)
        print(self.asal)
e=A(101,'chandani',3240034)
e.display()


















