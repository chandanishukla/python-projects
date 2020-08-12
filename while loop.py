i=1
while i<=10:
    print(i)
    i=i+1


i=1
while i<10:
    print(i)
    if i == 3:
        break
    i=i+1 # 1,2,3

i=1
while i<10:
    if i==3:
        break
    print(i)
    i=i+1 #1,2
i=1
while i<10:
    if i==3:
        continue
    print(i)
    i=i+1 #1 2



a=['foo','bar','baz','quiz']
s='corge'
i=0
while i <len(a):
    if a[i]==s:
        break
        i=i+1
    else:
        print(s,'not found in list') # infinite loop




n=int(input("Enter the number : ")) #number is Armstron or not
o=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if o==sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")


string="welcome to python"
i='o'
while i in string:
    print(i,end=" ")
    break
else:
    print("none") # o check o is present in string or not



