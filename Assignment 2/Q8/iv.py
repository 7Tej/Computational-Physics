from numpy import *
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *

# Defining the function representing for dy/dt = f(t, y)
def func(t,y):
    return cos(2*t)+sin(3*t)

# Defining the initial condition y(0)
y0 = 1

t_span = (0,1)
t=t_eval=linspace(0, 1, 101)
#Using Mathematica
def y_exact(t):
    return (1/6)*(8-2*cos(3*t)+3*sin(2*t))


def num_sol(t_span,y0,t_eval):
    sol = solve_ivp(func, t_span, [y0], t_eval=t_eval)
    return sol.t, sol.y[0]

t_, y = num_sol(t_span,y0,t_eval)

# Plotting the solution
plot(t_, y,'r*', markersize=3, label='Numerical Solution')
plot(t,y_exact(t), linewidth=2, label= 'Analytical Solution')

xlabel(r't$\rightarrow$')
ylabel(r'y(t)$\rightarrow$')
title(r"Solution to $y'=cos(2t)+sin(3t)}$")

legend()
grid(True)
show()
