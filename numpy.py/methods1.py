import numpy as np
# searching
arr=np.array([1,2,3,4,3,9])
s=np.where(arr==3)  #shows indexing of 3
print('even numbers index:',np.where(arr%2==0)) 
print(s)
#search sorted -> return index value
t=np.searchsorted(arr,3)
print(np.searchsorted(arr,3,side='right'))
print(t)

#sort
sort=np.sort(arr)
print(sort)

#filtering array

arr1=np.array([1,2,7,9,3,2,433,6,67,1,7,10,12])
filtered_array=[]
for i in arr1:
    if i>10:
        filtered_array.append(True)
    else:
        filtered_array.append(False)
newarr = arr1[filtered_array]
print(filtered_array)
print(newarr)

#random 

from numpy import random

r=random.randint(100)
print(r)
#rand method generate 0 to 1 float numbers.
ra=random.rand()
print(ra)
#create random array
arr2=random.randint(100,size=5)#size parameter specify the shape of an array.
print(arr2)
#2d array with 4 rows
ar=random.randint(100,size=(3,4)) #3rows  4 columns
print(ar)

#generate random numbers from array
a=random.choice([1,2,3,4])
print(a)
b=random.choice([1,2,3,4],size=(3,4))
print(b)