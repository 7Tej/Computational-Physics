""" This code compares 10000 random numbers between (0,1) generated using LCG( Linear Congruential 
Random Numbers Generator with the uniform PDF by plotting a density histogram
"""
from numpy import *
from matplotlib.pyplot import *

# LCG parameters
m = 4846834681 
a = 70
c = 77
xo = 7

#Total number of random numbers
n = 10000 

# To generate random numbers
def LCG(m,a,c,xo,n):
    random_numbers = []
    x = xo
    for i in range(n):
        x = (a * x + c) % m
        random_numbers.append(x / m)
    return random_numbers

# Generates 10,000 random numbers
random_numbers = LCG(m,a,c,xo,n)


# Plots density histogram
hist(random_numbers, bins=30, density=True, alpha=0.6, color='c', edgecolor='black')

# Uniform PDF
x = linspace(0, 1, 100)
uniform_pdf = [1] * len(x)  # Uniform PDF between 0 and 1 is a constant value of 1
plot(x, uniform_pdf, 'r--', linewidth=2)

title('Density Histogram of LCG Random Numbers vs Uniform PDF')
xlabel('Random Numbers')
ylabel('Density')
legend(['Uniform PDF', 'LCG Random Numbers'])
show()
"""Observation: larger is the m, more uniform is the density histogram"""
