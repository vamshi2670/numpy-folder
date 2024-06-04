import numpy as np
from numpy import random
#The shuffle() method makes changes to the original array itself.
arr=np.array([1,2,3,4])
random.shuffle(arr)
print(arr)

#The permutation() method returns a re-arranged array (and leaves the original array un-changed).
p=random.permutation(arr)
print(p)

                #seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. 
# It will be used to visualize random distributions.
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0,1,2,3,4,5])
plt.show()

#without hist
sns.distplot([1,2,3,4,5],hist=False)
plt.show()

#normal data distribution ->continous
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.

x=random.normal(size=(2,3))
print(x)

#binomial distribution ->descrete series
# n - number of trials.
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
# size - The shape of the returned array.

y=random.binomial(n=10,p=0.5,size=10)
print(y)

#poisson distribution -> estimates how many times an event can happen in a specified time
# lam - rate or known number of occurrences e.g. 2 for above problem.
# size - The shape of the returned array.

z=random.poisson(lam=3,size=10)
print(z)

#uniform distribution
# Used to describe probability where every event has equal chances of occuring.
# E.g. Generation of random numbers.
# It has three parameters:
# a - lower bound - default 0 .0.
# b - upper bound - default 1.0.
# size - The shape of the returned array.

a=random.uniform(size=(2,3))
print(a)

#logistic
# Logistic Distribution is used to describe growth.
# Used extensively in machine learning in logistic regression, neural networks etc.
# It has three parameters:
# loc - mean, where the peak is. Default 0.
# scale - standard deviation, the flatness of distribution. Default 1.
# size - The shape of the returned array.

b=random.logistic(loc=2,scale=4,size=(2,4))
print(b)
