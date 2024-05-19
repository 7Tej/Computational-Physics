"""Comparison of time to generate 10000 random numbers between (0,1)
 using LC random number generator and numpy.random.rand()"""
 
from numpy import *
from matplotlib.pyplot import *
from timeit import *

"""Using timeit for more precise time measurements"""


def LCG(m,a,c,xo,n):
    random_numbers = []
    x = xo
    for i in range(n):
        x = (a * x + c) % m
        random_numbers.append(x / m)
    return random_numbers

def LCG_random():
    # LCG parameters
    m = 4846834681 
    a = 70
    c = 77
    xo = 7

    #Total number of random numbers
    n = 10000 
    # Generates 10,000 random numbers
    random_numbers = LCG(m,a,c,xo,n)

t_LCG= timeit(LCG_random, number=1)
print('Time taken by Linear Congruential Generator to generate 10,000 random numbers =',t_LCG,'s')

def numpy_random():
    
    # Generates 10,000 uniformly distributed random numbers between 0 and 1
    random_numbers = random.rand(10000)
    
t_rand= timeit(numpy_random, number=1)

print('Time taken by numpy.random.rand(10000) =',t_rand,'s')
