import numpy as np
#lcm & gcd
n=4
n1=6
print(np.lcm(n,n1))
print(np.gcd(n,n1))

#trignometry
#sin cos tan
x=np.sin(np.pi/2)
print(x)

#convert degree to radian
arr=np.array([90,120,360,180])  
y=np.deg2rad(arr) #rad2deg()
print(y)

#finding angles -sin, cos and tan- functions arcsin, arccos, arctan .
print(np.arcsin(arr))
#hypot
a=4
b=6
print(np.hypot(a,b))
                        #Set
#find unique elements
arr1=np.array([1,3,4,6,6])
print(np.unique(arr1))
arr2=np.array([2,4,5,6,7])
print(np.union1d(arr1,arr2))
#intersection
print(np.intersect1d(arr1,arr2))
#set difference
print(np.setdiff1d(arr1,arr2))
#setXor1d values not present in both.
print(np.setxor1d(arr1,arr2))