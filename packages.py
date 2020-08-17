import pandas as pd
import numpy as np
dict1={
"Name":['harry','rohan','skillf','shubh'],
"Marks":[92,34,24,17],
"City":['rampur','kolkata','barailly','satna'] # i have created one dictionary
}
fd=pd.DataFrame(dict1) # creates the dataframe for faster access of data #dataframe is a excel sheet which we can use inside the python
print(fd)
fd.to_csv("file.csv") #creates the excel file
fd.to_csv("file_index_false.csv",index=False)# index=false command will not show index number to us
print(fd.head(2))# display first two rows
print(fd.tail(1))#display the last record ..we need to display the number of rows we want to access otherwise it will display the whole record
print(fd.describe()) #it will calculate count,mean min max ,50%,25% of all th numberic column
file1=pd.read_csv("file_cm.csv")
print(file1)
print(file1['speed'])# it will print the  whole speed column
print(file1['speed'][0])#print the value  of speed at 0 th column
print(file1['speed'])[3]=40#error
print(file1)
file1.to_csv("file1.csv")
file1.index=['First','Second','Third','Fourth','Fifth','SIX'] #we can change the index name
print(file1)
print(type(file1))#dataframe
print(type(file1['speed']))#series
ser=pd.Series(np.random.rand(34))#it will create series of 0 to 33
print(ser)








newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
print(newdf)
print(type(newdf))#dataframe
print(newdf.describe())
print(newdf.dtypes)
print(newdf.head(3))
newdf[0][0]="harry" #it will 0,0 as object
print(newdf.dtypes)
print(newdf)# include harry in 0,0 place
print(newdf.head(3))
print(newdf.index)#print the indexes
print(newdf.columns)
print(newdf.to_numpy())
print(newdf.T)#rows converted into column and column into rows row=4 and column=334
print(newdf.sort_index(axis=0,ascending=False))# axis=0(rows) by deafult ascending in increasing order
print(newdf.sort_index(axis=1,ascending=False))#axis=1(column)sort on the bases of column

print(type(newdf[0]))#the combination of series creates a dataframe#series datatype
newdf2=newdf
newdf2[0][0]=6659
# print(newdf2)#it will create copy which point to the same object
print(newdf)# if we change the value of  newdf2 then the  value of new will autamatically change# view in data frame

newdf2=newdf.copy()
newdf2[0][0]=44354
# print(newdf2)#copy ..if we change one data frame then the other will not effect
print(newdf)

newdf.columns=list('ABCDE') #converting the column name into abcde
# print(newdf)
newdf.loc[0,0]=5646646#it will create a new column with 0 and print the value 0 to 0 and print rest of the value NAN
print(newdf)#using loc will not give error
newdf.columns=list('ABCDE')
newdf.loc[0,'A']=54484928
print(newdf)

print(newdf.loc[[1,2],['C','D']])#two row and two column
print(newdf.loc[:,['C','D']])#all the rows of c and d column
print(newdf.loc[[1,2],:])#two row and all the columns
print(newdf.loc[(newdf['A']==0.3)])
print(newdf.iloc[0,4]) #it will print 4 column value
print(newdf.iloc[1,3])#if we want to fetch the value using index then we will use iloc and if we want to acess value by using name the we will use loc
print(newdf.drop(0))#it deletes the zero row
print(newdf.drop(['A'],axis=1))#column1 droped
print(newdf.drop(['A','C'],axis=1))#A and c will be droped

newdf.drop([0,6],axis=0,inplace=True) #this command will remove thespecified column from the original list
print(newdf)
print(newdf.reset_index()) #this command will set the rows values from 0 to the specified values but it will also create one column with index name
print(newdf.reset_index(drop=True,inplace=True))
print(newdf['B'].isnull())# return the column as true if null value is avalible otherwise it will  return false
newdf.loc[:,['A']]=None
print(newdf)# it will ser the whole cloumn A as None
newdf['A'].isnull()
print(newdf)
newdf.loc[:,['A']]=56
print(newdf)# will  set the whole column a as 56
newdf.dropna()#it will remove the na from the dataframes

#new dataframe
df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
# print(df)
l=df.drop_duplicates(subset=['brand'])
print(l)











