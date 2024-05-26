
""" This code generates random numbers following distribution sqrt(2/pi).exp(-0.5x^2)
    by Rejection method using the envelope func g(x) = sqrt(2/pi){1 if 0<x<4 , 0 o.w}"""
    
from numpy import*
from matplotlib.pyplot import *

def f(x):
    return sqrt(2/pi) * exp(-0.5 * x**2)

# Number of samples we want
n = 700
random_numbers = []

while len(random_numbers) < n:
    
    # Generates x values from a uniform distribution scaled to [0, 4]
    x = random.rand(n)*4 
    
    # Generates y values from a uniform distribution scaled to [0, sqrt(2/pi)]; top hat
    y = random.rand(n) * sqrt(2/pi)
    
    f_ = f(x)
    
    # Accepts samples where y < f(x)
    x_good = x[y < f_]
    y_good = y[y < f_]
    
    x_bad = x[y > f_]
    y_bad = y[y > f_]
    
    # Adds the accepted samples to the list of samples
    random_numbers.extend(x_good)
    
    # Ensures only num_samples are kept
    random_numbers = random_numbers[:n]

random_numbers = array(random_numbers)

scatter(x_good,y_good,marker = '.', label = 'Accepted points')
scatter(x_bad,y_bad, c='red',marker = '.', label = 'Rejected points')

# Plots the histogram of the samples
hist(random_numbers, bins=20, density=True, alpha=0.6, edgecolor= 'black', label='Density Histogram')


# Plots the target distribution for comparison
x = linspace(0, 4, 1000)
plot(x, Gaussian(x), 'r', lw=2, label='Target pdf')

xlabel(r'x$\rightarrow$')
ylabel(r'Density$\rightarrow$')
xlim(0,5)
legend()
title('Rejection Method for $f(x) = \\left(\\frac{2}{\\pi}\\right)^{0.5} e^{-0.5x^{2}}$')
show()
