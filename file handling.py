# f=open(filename,'mode')

f=open('Python_class1.txt','w')
print('Name :',f.name) # abc.txt
print('Mode :',f.mode) # w
print('closed :',f.closed)# False
print('Readable :',f.readable())#  False
print('writeable :',f.writable())# True


f=open('Python_class1')
print('Name :',f.name)#abc.txt
print('Mode :',f.mode)#r
print('closed :',f.closed)#False
print('Readable :',f.readable())#True
print('writeable :',f.writable()) #False
f.close()
print('closed :',f.closed) #closed : True



#FileExistsError: [Errno 17] File exists: 'abc.txt' because abc file is already available
f=open('Python_class1.txt','x')
print('Name :',f.name)
print('Mode :',f.mode)
print('closed :',f.closed)
print('Readable :',f.readable())
print('writeable :',f.writable())
f.close()
print('closed :',f.closed)





f=open('Python_class2.txt','x') #new file is created
print('Name :',f.name)#xyz.txt
print('Mode :',f.mode)#x
print('closed :',f.closed)#False
print('Readable :',f.readable())#False
print('writeable :',f.writable())#True
f.close()
print('closed :',f.closed)#True


f=open('Python_class2.txt','x')
print('closed :',f.closed) #False
f.close()
print('closed :',f.closed)#True


#writing data to the file
#doesnt matter how many time we will execute the file ,it will overwrite the file and data will available only one time
#if we dont want overwritethe prwevious data the we will use append
f=open('Python_class3.txt','w')
f.write("Hii!!\n")
f.write("Python\n")
f.write("Django\n")
print("Data entered sucessfully ")
f.close()

#overwriting will not be done
f=open('Python_class3.txt','a')
f.write("Hii!!\n")
f.write("Python\n")
f.write("Django\n")
print("Data entered sucessfully ")
f.close()


#writeline
f=open('Python_class4.txt','w')
list=['hii\n','python\n','hello']
f.writelines(list)
print("all the data  are written sucessfully")
f.close()

#reading data from the file
f=open('Python_class4.txt','r')
data=f.read() #reading all the data from the file
print(data)
f.close()



f=open('Python_class4.txt','r')
data=f.read(6) #only read 6 characters from the file including back slash n also
print(data)
f.close()

f=open('Python_class4.txt','r')
data=f.read(6) #only read 6 characters from the file including back slash n also
print(data)
f.close()

#to read data line by line
f=open('Python_class4.txt','r')
line=f.readline() #only read first lline
print(line,end="")
line2=f.readline() #read the second line
print(line2,end="")
f.close()

f=open('Python_class4.txt','r')
lines=f.readlines()# read al the list element
for line in lines:
    print(line,end="")


f1=open('input_file.txt','r')
f2=open('output_file.txt','w')
f2.write(f1.read())
f1.close()
f2.close()
print("data copied sucessfully")




with open('Python_class5.txt','w')as f:
    f.write("hey\n")
    f.write("python\n")
    f.write("hello")
    print("Is file closed",f.closed)#false(not closed) because it is inside the with statement only
print("Is file closed",f.closed)#automatically closed


f= open('Python_class3.txt', 'r')
print(f.tell())#point the current position of cursor#0
print(f.read(2))
print(f.tell())#2
print(f.read(4))
print(f.tell())#7


data= "All Students are STUPIDS"
f=open( "abc.txt" , "w" )
f.write(data)
with open( "abc.txt" , "r+" ) as f:
    text=f.read()
    print(text)
    print ( "The Current Cursor Position: " ,f.tell())
    f.seek( 17 )
    print ( "The Current Cursor Position: " ,f.tell())
    f.write( "GEMS!!!"	)
    f.seek( 0 )
    text=f.read()
    print ( "Data After Modification:"	)
    print (text)



import os
fname=input("Enter the file name : ")
if os.path.isfile(fname):
    print("file Exists :",fname)
    f=open(fname,'r')
    print("the content of the file is ")
    print(f.read())
else:
    print("file dosent exist",fname)



f1=open( "rossum.jpg","rb" )
f2=open( "newpic.jpg","wb" )
bytes=f1.read()
f2.write(bytes)
print ( "New Image is available with the name: newpic.jpg")



import csv
with open( "emp.csv", "w" ,newline=	'' ) as f:
    w=csv.writer(f)	# returns csv writer object
    w.writerow(["ENO" , "ENAME" , "ESAL" , "EADDR" ])
    n=int(input(	"Enter Number of Employees:"	))
    for i in range(n):
        eno=input(	"Enter Employee	No:" )
        ename=input(	"Enter Employee	Name:" )
        esal=input(	"Enter Employee	Salary:" )
        eaddr=input(	"Enter Employee	Address:"	)
        w.writerow([eno,ename,esal,eaddr])
print ( "Total Employees	data written to csv file successfully"	)
