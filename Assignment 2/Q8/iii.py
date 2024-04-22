from numpy import *
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *

# Defining the function representing for dy/dt = f(t, y)
def func(t,y):
    return 1+(y/t)

# Defining the initial condition y(0)
y0 = 2

t_span = (1,2)
t=t_eval=linspace(1, 2, 101)
#Using Mathematica
def y_exact(t):
    return 2*t+t*log(t)


def num_sol(t_span,y0,t_eval):
    sol = solve_ivp(func, t_span, [y0], t_eval=t_eval)
    return sol.t, sol.y[0]

t_, y = num_sol(t_span,y0,t_eval)

# Plotting the solution
plot(t_, y,'r*', markersize=3, label='Numerical Solution')
plot(t,y_exact(t), linewidth=2, label= 'Analytical Solution')

xlabel(r't$\rightarrow$')
ylabel(r'y(t)$\rightarrow$')
title(r"Solution to $y'=1+\frac{y}{t}$")

legend()
grid(True)
show()
