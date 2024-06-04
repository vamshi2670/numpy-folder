import numpy as np
from numpy import random
import seaborn as snc
import matplotlib.pyplot as plt

#multinomial
# Multinomial distribution is a generalization of binomial distribution.
# It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. 
# e.g. Blood type of a population, dice roll outcome
# n - number of possible outcomes (e.g. 6 for dice roll).
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.

a=random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6,])
print(a)

#exponantial distribution
#Exponential distribution is used for describing time till next event e.g. failure/success etc
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
# size - The shape of the returned array.
b=random.exponential(scale=2,size=(1,2))
print(b)

#chi square distribution
# Chi Square distribution is used as a basis to verify the hypothesis.
#df - degree of freedom and size
c=random.chisquare(df=2,size=(2,4))
print(c)

#Reyligh distribution
#Rayleigh distribution is used in signal processing. scale,size
d=random.rayleigh(scale=4,size=3)
print(d)

#pareto distribution
#A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).
#a - shape of parameter ,size
e=random.pareto(a=2,size=(2,3))
print(e)

#zipf distribution
#Zipf distributions are used to sample data based on zipf's law.
#a-distribution parameter ,size
f=random.zipf(a=3,size=3)
print(f)