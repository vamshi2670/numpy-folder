#copy
import numpy as np
arr=np.array([1,2,3,4])
x=arr.copy()
x[1]=32   
print(arr)
print(x)  #here only x change

#for both arrays change
y=arr.view()
y[0]=32
print(arr)
print(y)

#shape
arr1=np.array([[1,2,3,4],[5,6,7,8]])
print(arr1.shape)  #(dimensions,no.of elements)

#reshpe 1d to 2d
print(arr.reshape(2,2))
#1d-3d
arr2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr2.reshape(2,3,2)) #2array in contain 3 arrays each array 2 elements.
print(arr1.reshape(-1)) #convert flat array.

#iterator
#id array
for x in arr:
    print(x)
#2d array
for x in arr1:
    for y in x:
        print(y)
#iterator-> using nditer() function

for i in np.nditer(arr1,flags=["buffered"],op_dtypes=['S']):
    print(i)

#joining arrays ->two or more arrays are merging.
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.concatenate((a,b))
print(c)
#hstack
d=np.hstack((a,b))
print(d)
#vstack
print(np.vstack((a,b)))
#hstack
print(np.hstack((a,b)))
print(np.dstack((a,b)))

#split syntax:array_split(array,num)
#split is not adjust elements if less or more.it did adjusting.
e=np.array_split(a,2)
print(e)
print(np.hsplit(a,1)) #horzontali split
print(np.hstack(a))
print(np.vsplit(a))
print(np.vstack(a))

