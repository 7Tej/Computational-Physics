import numpy as np
from matplotlib.pyplot import *

# To Define the ordinary differential equation (ODE)
def ode(x, u):
    return 1/((((1-u)*x)**2) + u**2)

# To Implement the fourth-order Runge-Kutta (RK4) method
def rk4(ode, x0, u, h):
    k1 = ode(x0, u)
    k2 = ode(x0 + 0.5 * h * k1, u + 0.5 * h)
    k3 = ode(x0 + 0.5 * h * k2, u + 0.5 * h)
    k4 = ode(x0 + h * k3, u + h)
    return x0 + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

# To Define initial condition
x0 = 1

#To Define the range for u values
u0 = 0
uf = 1


# Number of steps
n_steps = 10**6
h = (uf-u0)/n_steps

# To Initialize arrays to store u and x values
u_values = np.linspace(u0, uf, n_steps)
x_values = np.zeros_like(u_values)

# To Use RK4 method to solve the ODE
x = x0
for i in range(n_steps):
    x_values[i] = x
    x = rk4(ode, x, u0 + i * h, h)

# To Print the solution at a specific value of the argument
target_u = 3.5*(10**6)/(1+3.5*(10**6))  # Value of the argument 
print("Solution at t=3.5*10^6 or u =", target_u, "is x =", x)
plot(u_values, x_values, label='RK4')
title(r"Solution for $\frac{dx}{du} = \frac{1}{(1-u)^2 x^2 +u^2}; u=\frac{t}{1+t}$")
xlabel(r"u$\rightarrow$")
ylabel(r"x$\rightarrow$")
grid(True)
legend()

show()
