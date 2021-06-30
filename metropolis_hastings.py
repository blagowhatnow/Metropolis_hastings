#Metropolis Hastings algorithm

import numpy as np
import matplotlib.pyplot as plt

#Define a probability distribution function for.In this case, it's a gaussian at mean 0 and std 1

def func(x):
    res=1/np.sqrt(2*np.pi)*np.exp(-(1/2)*(x**2))
    return res

#Sample n=100000 instances of the random variable

x=np.zeros(100000)

x[0]=3.0

for i in np.arange(1,100000):
    cur_x=x[i-1]
    prop_x=cur_x+np.random.normal(0,1,1)
    A=func(prop_x)/func(cur_x)
    if A>np.random.uniform(1,0,1):
       x[i]=prop_x
    else:
       x[i]=cur_x

arg=np.arange(0,100000)
plt.scatter(arg,x)
plt.show()
