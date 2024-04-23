from pylab import *
from numpy import *

t0 = 1
y0 = -2
tf = 3
n = 1000
h = (tf - t0) / n

delta = 1e-4

def f(y, t):
    return ((y**2) + y) / t
def exact_sol(t_):
    return [-2*t_/(2*t_-1) for t_ in t_]

def RK4(f, t0, y0, h):
    k1 = h * f(y0, t0)
    k2 = h * f(y0 + k1 / 2, t0 + h / 2)
    k3 = h * f(y0 + k2 / 2, t0 + h / 2)
    k4 = h * f(y0 + k3, t0 + h)
    k = (k1 + 2 * k2 + 2 * k3 + k4) / 6
    yn = y0 + k

    return yn

t_values = []  # List to store t values
y_values = []  # List to store y values

mesh_points = []  # List to store mesh points

t = t0
y = y0

#Adaptive Step-size Control

while t < tf:
    t_values.append(t)
    y_values.append(y)
    rho = 0
    while rho < 1:
        y1 = RK4(f, t, y, h)
        y2 = RK4(f, t+h, y1, h)
        y3 = RK4(f,t,y,2*h)
        eps= abs(y3-y2)/30
        rho = h*delta/eps
        h = h*rho**(0.25)
        
    y= y1
    t+= h
    
# To plot y vs t
plot(t_values, y_values,'ro',label='mesh points')
plot(t_values, y_values,'b-',label='Numerical solution')
plot(t_values, exact_sol(t_values),label='Exact Solution')

title(r"Adaptive Step-size Control with RK4 for  y' = $\frac{y^2+y}{t}$")
xlabel(r"t$\rightarrow$")
ylabel(r"y$\rightarrow$")
legend()
grid(True)
