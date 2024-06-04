#ufuncs stands for univarsal functions
#ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# where -boolean array or condition defining where the operations should take place.
# dtype- defining the return type of elements.
# out- output array where the return value should be copied.

#create functions
#frompyfunc() 
# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.
import numpy as np
def myadd(x,y):
    return x+y
myadd=np.frompyfunc(myadd,2,1)
print(myadd([1,2,3],[4,5,6]))

#add function sum two arrays
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
c=np.add(a,b) #subract,multiply,divide,power,mod,reminder,divmod,absolute
print(c) #above functions also use.

#trunc  and fix ->remove decimal return float close to zero.
d=np.trunc([2.44,-2.32])
print(d)
#around -> 
e=np.around([3.1666],2) #2 for no.of decimal places.
print(e)
#floor-nearst integer,ceil-highest integer.
f=np.floor([2.33])
print(f)

#logs ->Use the log() function to perform log at the base custom.
g=np.arange(1,10)
h=np.log(g) #log2,log10 use with base.
print(h)

arr=[1,2,4,5]
arr1=[5,3,4,2]
print(np.sum([arr,arr1],axis=1)) #sum numbers in array

#cumulative sum -[1,1+2,1+2+3]=out put[1,3,6]
print(np.cumsum(arr))

#product of the elements in an array, use the prod() function
print(np.prod(arr))
print(np.cumprod(arr))

#difference
print(np.diff(arr)) #[2-1 4-2 5-4]
