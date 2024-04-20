#RK-4
from math import *
from numpy import *
from matplotlib.pyplot import *

# y' = u
# u' = -y
#defining the differential eqn

def F(y, u, x):
    return 2*u-y+x*exp(x)-x
 
#params
a = 0
b = 1.0
N =1000
h = (b-a)/N

#initiating arrays
x_vals = arange(a,b,h)
y_vals = []
u_vals = []

#initial values
y = 0.0
u = 0 

#implementing RK-4
for x in x_vals:
    y_vals.append(y)
    u_vals.append(u)

    m1 = h*u
    k1 = h*F(y, u, x)  #(y, y', x)

    m2 = h*(u + 0.5*k1)
    k2 = h*F(y+0.5*m1, u+0.5*k1, x+0.5*h)

    m3 = h*(u + 0.5*k2)
    k3 = h*F(y+0.5*m2, u+0.5*k2, x+0.5*h)
    
    m4 = h*(u + k3)
    k4 = h*F(y+m3, u+k3, x+h)

    y += (m1 + 2*m2 + 2*m3 + m4)/6
    u += (k1 + 2*k2 + 2*k3 + k4)/6

plot(x_vals, y_vals)
title(r"Solution for $\frac{d^{2}y}{dx^2} =2 \frac{dy}{dx} -y + xe^{x} -x$")
xlabel(r"x$\rightarrow$")
ylabel(r"y$\rightarrow$")
grid(True)

show()
