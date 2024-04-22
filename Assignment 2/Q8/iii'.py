from numpy import *
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *

# Defining the function representing for dy/dt = f(t, y)
def func(t, y):
    return 1+(y/t)

# Defining the initial condition y(0)
y0 = 2

t_span = (1,2)
t=t_eval=linspace(1, 2, 101)
#Using Mathematica
y_exact = array([2.,2.03005,2.0602,2.09045,2.12079,2.15123,2.18177,2.21239,2.24312,2.27393,2.30484,2.33584,2.36693,2.39811,2.42937,2.46073,2.49217,2.52369,2.55531,2.587,2.61879,2.65065,2.6826,2.71463,2.74674,2.77893,2.8112,2.84355,2.87598,2.90849,2.94107,2.97374,3.00647,3.03929,3.07218,3.10514,3.13818,3.17129,3.20448,3.23773,3.27106,3.30446,3.33793,3.37147,3.40509,3.43877,3.47252,3.50634,3.54022,3.57418,3.6082,3.64229,3.67644,3.71066,3.74494,3.7793,3.81371,3.84819,3.88273,3.91734,3.95201,3.98674,4.02153,4.05639,4.0913,4.12628,4.16132,4.19642,4.23157,4.26679,4.30207,4.3374,4.3728,4.40825,4.44376,4.47933,4.51495,4.55063,4.58637,4.62217,4.65802,4.69392,4.72988,4.7659,4.80197,4.83809,4.87427,4.9105,4.94679,4.98313,5.01952,5.05597,5.09246,5.12901,5.16561,5.20227,5.23897,5.27573,5.31253,5.34939,5.38629])


def num_sol(t_span,y0,t_eval):
    sol = solve_ivp(func, t_span, [y0], t_eval=t_eval)
    return sol.t, sol.y[0]
    
t_, y = num_sol(t_span,y0,t_eval)

# Plotting the solution
plot(t_, y,'r:', label='solve_ivp( )')
plot(t,y_exact, label= 'Mathematica')

xlabel(r't$\rightarrow$')
ylabel(r'y(t)$\rightarrow$')
title(r"Solution of $y'=1+\frac{y}{t}$")

legend()
grid(True)
show()
