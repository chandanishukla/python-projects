def fun():
    print("Welcome to the university...")
fun()


def fun1():
    print("Hii")
def fun2():
    print("Python")
def fun3():
    print("byee")
fun1()
print("Byee Byee ! ")
fun3()



def fun1():
    print("sathya technology ")
    f2() ## name 'f2' is not defined....we need to define the function before calling it
    print("fgfd")
fun1()
print("byeee")



def fun1():
    print("python")
    fun2()
    print("venket")
def fun2():
    print("reddy")
fun1()
print("byeee")


def sum(a,b):
    print("the total value is :",a+b) # function with argument
sum(20,30)

# function with return type
def sum(a,b):
    c=a+b
    return c
p=int(input(" the the value osf p : ")) #function with argument and return tpe enter the values dynamically
q=int(input(" the the value osf q : "))
r=sum(p,q)
print(r)


def sum(a,b):
    c=a+b
    return c #with argument with return type
r=sum(3,4)
print(r)


def total(s1,s2,s3):
    c=s1+s2+s3
    return c
total1=total(2,4,3)
print(total1)

def employeedetail(eid,ename,salary):
    print("Employee id is : ",eid)
    print("Employee name is : ",ename) #positional argument
    print("Employee salary is : ",salary)
employeedetail(101,'Chandani',20000)


def sum(a,b):
    c=a+b
    return c
x=sum(2,3)
print(x)

# function with no argument and no return type
def sum():
    a=int(input("Enter the value of a : "))
    b=int(input("Enter the value of b : "))
    c=a+b
    print("The value of a and b is: ",c)
sum()

# function with argument and without return type
def sum(a,b):
    c=a+b
    print(c)
sum(2,8)


# function with no argument and with return type
def sum():
    a=20
    b=30
    c=a+b
    return c
p=sum()
print(p)


#function with argument with return type
def sum(a,b):
    c=a+b
    return c
d=sum(10,30)
print(d)


#positional argument
def empinfo(eid,ename,esal):
    print("Enter the ID : ",eid)
    print("Enter the Name : ",ename)
    print("Enter the salary : ",esal)
empinfo(101,'chandani',1002)


#keyword argument
def empinfo(eid,ename,esal):
    print("Enter the ID : ", eid)
    print("Enter the Name : ",ename)
    print("Enter the salary : ",esal)
empinfo(eid=101,ename='chandani',esal=1234000)



#default argument
def emp(eid,ename,esal='nam'):
    print("Enter the ID : ", eid)
    print("Enter the Name : ",ename)
    print("Enter the salary : ",esal)
emp(101,'chandani')


#variable length argument
def empinfo(*d):
    print(d)
empinfo(101,'chandani',120044)

#variable keyword argument
def msg(**kwargs):
    for k,v in kwargs.items():
        print(k,"......",v)
msg(m=10,n=20,p=30,s=1)













