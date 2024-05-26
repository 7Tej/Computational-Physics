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

    
""" Volume of a 10-d hyper sphere """

dimensions = 10

# Generates random points in 10 dimensions within the bounds [-1, 1]
point = random.uniform(-1, 1, size=(n, dimensions))

# Determines if a point lies within the 10-dimensional unit hypersphere
inside_hypersphere = sum(point**2, axis=1) <= 1

# Counts the number of points inside the hypersphere
points_inside_hypersphere = sum(inside_hypersphere)

# Calculates the volume of the 10-dimensional unit hypersphere
volume_hypersphere = (points_inside_hypersphere / n) * (2**dimensions)

print('Obtained volume of the 10-dimensional unit hypersphere =', volume_hypersphere)
