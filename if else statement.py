n=int(input("Enter the number : "))
if n>0:
    print("given number is positive ")
else:
    print("thank you")


age=int(input(" Enter the age : "))
if age>18:
    print("eligible for volte ")
else:
    print("better luck next time ")



choice=int(input("enter your choice : "))
if choice==1:
    cost=40000
    print("cost of laptop is:",cost)
    q=int(input("enter quality : "))
    total=cost*q
    print("total bil is : ",total)
elif choice==2:
    cost=50000
    print("cost of desktop is:", cost)
    q = int(input("enter quality : "))
    total = cost * q
    print("total bil is : ", total)
elif choice==3:
    cost=60000
    print("cost of Tab is:", cost)
    q = int(input("enter quality : "))
    total = cost * q
    print("total bil is : ", total)
elif choice==4:
    cost=100000
    print("cost of Mobile is:", cost)
    q = int(input("enter quality : "))
    total = cost * q
    print("total bil is : ", total)





Mage=int(input("Enter Man age : "))
Wage=int(input("Enter Women age : "))
if Mage>28 and Wage>25:
    print("Couple is eligible for marriage ")
else:
    print("couple is not eligible for marriage")





esalary=int(input("enter the employee salary : "))
asal=esalary*12
print("annual salary is : ",asal)
if(asal>50000):
    intax=asal*0.2
    pf=asal*0.1
    saving=asal*1.5
print("income tax paid",intax)
print("pf paid : ",pf)
print("savings",saving)


product1=int(input("Enter the cost : "))
product2=int(input("Enter the cost : "))
product3=int(input("Enter the cost : "))
total=product1+product2+product3
print("Total is : ",total)
if total>5000:
    finalbill=total*0.2
    print("finalbill is : ",finalbill)


string=input("Enter the string :") #given number is palandrome or not
rev_string=string[: :-1]
if string==rev_string:
    print("given string is palindrome ")
else:
    print("given string is not palindrome")

gender=input("enter the gender of member1 : ")
if gender=='male':
    print("book seat")
else:
    print("not allowed to book seat")