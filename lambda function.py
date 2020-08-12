#Lambda function
a=lambda x:x**2
print(a(8)) #square of number

a=lambda x,y:x+y
print(a(30,40)) # addition of two number using lambda function

a=lambda x: x%2==0
print(a(4)) #given number is even


a= lambda x:x%2==0
n=int(input("enter the number:")) # through user input
if a(n):
    print("given number is even:",n)
else:
    print("given number is odd:",n)


x=lambda a,b: a if a>b else b
print(x(300,500))


#filter function
L=[4,2,3,6,8,9,1,8,6]
x=list(filter(lambda a:a%3!=0,L))
print(x)# number divide by 3 does not equal to zero

lst=[4,5,6,8,7,3,2,9]
t=tuple(filter(lambda x:x%2==0,lst))
print(t)

lst=[4,2,6,8,95,-1,-3,-5]
L1=list(filter(lambda x:x<=0,lst))
print(L1)

#map function
lst=[2,4,4,3,5,6,7,9]
l=set(map(lambda x:x**2,lst))
print(l)

lst=[2,4,3,6,57,9,8,1]
l=set(map(lambda x:x+2,lst))
print(l)

lst=[4,2,6,8,6,5,4]
s=list(map(lambda x:x/2,lst))
print(s)


#reduce function
import functools as f
lst=[2,5,6,8,79,4,6]
s=f.reduce(lambda x,y:x+y,lst)
print(s)

import functools as fb
lst=[2,8,6,9,8,4,5,3]
p=fb.reduce(lambda x,y:x*y ,lst)
print(p)