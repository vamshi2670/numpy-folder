'numpy is python library used for working with arrays'
#numpy stands for numarical python it is 50X faster than lists.

import numpy as np

#syntax:variable=numpy.array(iterator) means send list or tuple anythig.
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))

#0D array

arr1=np.array(4)
print(arr1)

#1d array

arr2=np.array([1,2,3,4])
print(arr2)
#An array that has 1-D arrays as its elements is called a 2-D array.
#as like all
#2d array

arr3=np.array([[1,2,3],[4,5,6]])
print(arr3)

#3d array

arr4=np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])
print(arr4)

#check no.of dimensions
#ndim attribute with know how many dimensions are there
a=np.array([[1,2,3],[2,3,4]])
print(a.ndim)

d=arr4.ndim
print(d)

#here creating dimensions with ndmin

b=np.array([1,2,3],ndmin=4)
print(b)

#accessing array elements
#where the dimension represents the row and the index represents the column.
c=np.array([[1,2,3],[5,6,7]])
print(c[0,1])  # 6 for print(c[1,2]) 

d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(d[0,1,2])

#array slicing : syntax:[start:end:step]
e=np.array([1,2,3,4,5,6,7,8,9])
print(e[1:9:2]) #e[2:6]
f=np.array([[1,2,3],[4,5,6]])
print(f[1,1:3])

#data type | dtype  attribute with know datatype
print(f.dtype) #type check

g=np.array([[1,2,3],[2,3,4]],dtype="S") 
print(g.dtype)

#type conversation
h=np.array([[1,2,3],[2,3,4]])
i=h.astype('f')
print(i.dtype)
