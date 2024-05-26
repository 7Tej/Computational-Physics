""" Monte Carlo method of integration"""
from numpy import *

n = 1000000
points = random.uniform(-1,1,size = (n,2))

#To determine whether a point (x,y) is within x^2 + y^2 <=1 

inside_circle = sum(points**2, axis = 1) <=1
points_inside_circle = sum(inside_circle)

A = (points_inside_circle/n)*4 
print('Obtained area of the circle =', A)

""" o Area of the square in which the points are generated is 4,
    spanning (-1,1) for both x and y directions

    o fraction of points inside the circle is points_inside_circle/n
    o times the area of the square gives the area of the circle """
