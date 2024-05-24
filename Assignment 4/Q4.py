""" Plots Density histogram of the generated 10,000 random numbers in C
    and compares with the Exponential pdf(mean = 0.5)
"""
from numpy import *
from matplotlib.pyplot import *
Random = loadtxt("D:\\random.txt")

hist(Random, bins=50, density=True, label='Density Histogram')

l = 0.5
x = linspace(0, max(Random), 1000)
pdf =(1/l)*exp(-x/l)
plot(x,pdf,'r-',label='Exponential pdf')

xlabel(r'Random Number$\rightarrow$')
ylabel(r'Density$\rightarrow$')
legend()
