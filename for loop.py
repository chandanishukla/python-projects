
for i in range(5):
    print(i,end=" ")


for i in range(5,-1):
    print(i, end=" ") #nothing printing in result


for i in range(-1,5):
    print(i,end=" ") #-1 to 4


for i in range(0,11,2):
    print(i,end=" ")# even number between 0 to 10


for i in  range(0,10,3):
    print(i,end=" ") #0,3,9


fruits=['apple','banana','cherry']
for i in  fruits:
    print(i)


fruits=["apple","banana","cherry"]
for x in  fruits:
    if x=="apple":
        break
    print(x) # nothing will print


for x in range(2,30,3):
    print(x,end=" ")


x=[2,4,3,6,5,87,8]
y=[2,7,5,9,5,0]
for i in x:
    for j in y:
        print(i,j)


marks=[90,89,65,47,98]
for i in marks:
    print(i,end=" ")


name="chandani"
for i in name:
    print(i,end=" @ ")


for i in range(5,0,-1):
    print(i,end=" , ")


n=int(input("enter the numer : "))
for i in range(1,11):
    print(n,"*",i," = ",n*i)



for i in range(1,10):
    if i%2==0:
        break
    print(i,end=" ")
print("Thank you!") #1 thank you

for i in range(1,10):
    if i%2!=0:
        break
    print(i,end=" ") # nothing

for i in range(1,10):
    if i%2==0:
        continue
    print(i,end=" ") #1,3,5,7,9



x = ['ab', 'cd']
for i in x:
    i.upper()
print(x)

