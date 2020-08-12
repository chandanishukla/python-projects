s=[ 2**i for i in range(2)]
print(s)
s=[i for i in range(20) if i%2==0]
print(s)
s=[i for i in range(30) if i%2!=0]
print(s)

s=["chandani","shukla","hello"]
m=[i[0] for i in s]
print(m)
s=input("enter the name:")
for i in s:
     if i=='a'or i=='e'or i=='i'or i=='o' or i=='u':
      print(i)

s=input("enter the value:")
l=[i for i in s  if i=='a'or i=='e'or i=='i'or i=='o' or i=='u']
print(l)


import numpy as np
a =np.array([12,30,40,50])
print(a)

from numpy import *
a=array([10,20,30,40]) ## simple way
print(a)

a=linspace(1,20)
print(a)

ar=array([1,2,4,3,6,57,8])
ar1=array([4,8,6,8,0,3])
for i in ar:
    i=i+5
    print(i,end=" ")
print(sum(ar))
print(sin(ar))
print(cos((ar)))
print(log(ar))
print(sqrt(ar))
print(min(ar))
print(max(ar))
print(concatenate([ar,ar1]))
ar2=ar
print(ar2)
print(ar)
print(id(ar))
print(id(ar2))
ar=array([30,1,5,7,9,0,3])
ar1=ar.copy()
ar[2]=3
print(ar1)
print(ar)


ar=[]
n=int(input("enter the length ogf array:"))
for i in range(n):
    x=int(input("enter the values:"))
    ar.append(x)
print(ar)
ar=[]
for i in range(10):
    x=int(input("enter the number:"))
    ar.append(x)
print(ar)


























