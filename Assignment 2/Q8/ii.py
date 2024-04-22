from numpy import *
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *

# Defining the function representing for dy/dt = f(t, y)
def func(t,y):
    return 1-(t-y)**2

# Defining the initial condition y(0)
y0 = 1

t_span = (2,3)
t=t_eval=linspace(2, 2.99, 101)
#Using Mathematica
def y_exact(t):
    return ((1/(t-3))+t)


def num_sol(t_span,y0,t_eval):
    sol = solve_ivp(func, t_span, [y0], t_eval=t_eval)
    return sol.t, sol.y[0]

t_, y = num_sol(t_span,y0,t_eval)

# Plotting the solution
semilogy(t_, y,'ro', markersize=5, label='Numerical Solution')
semilogy(t,y_exact(t), linewidth=2, label= 'Analytical Solution')

xlabel(r't$\rightarrow$')
ylabel(r'y(t)$\rightarrow$')
title(r"Solution to $y'=1-(t-y)^{2}$")

legend()
grid(True)
show()
