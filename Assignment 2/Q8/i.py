from numpy import *
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *

# Defining the function representing for dy/dt = f(t, y)
def func(t, y):
    return t*exp(3*t)-2*y

# Defining the initial condition y(0)
y0 = 0

t_span = (0,1)
t=t_eval=linspace(0, 1, 100)


def num_sol(t_span,y0,t_eval):
    sol = solve_ivp(func, t_span, [y0], t_eval=t_eval)
    return sol.t, sol.y[0]
    
t, y = num_sol(t_span,y0,t_eval)

#Using Mathematica
def exact_sol(t):
    return 0.04*exp(-2*t)*(1-exp(5*t)+5*(exp(5*t)*t)) 

# Plotting the solution
plot(t, y, label='Numerical Solution')
plot(t, exact_sol(t),'r:',label = 'Exact Solution')
xlabel(r't$\rightarrow$')
ylabel(r'y$\rightarrow$')
title(r"Solution of $y'=te^{3t}-2y$")

legend()
grid(True)
show()
