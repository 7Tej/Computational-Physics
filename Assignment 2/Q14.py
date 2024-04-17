from numpy import *
from matplotlib.pyplot import *

# Defining the function f(t, y, y_prime)
def f(t, y, y1):
    return ((t**3) * log(t) + (2 * t * y1 - 2 * y) )/ (t**2)

# Defining the exact solution
def exact_solution(t):
    return 7 * t / 4 + ((t**3) / 2) *log(t) - (3 / 4) * t**3

# Parameters
t_ini = 1
t_fin = 2
y_ini = 1
y1_ini = 0
h = 0.001  # Step size

# Number of steps
n = int((t_fin - t_ini) / h)

# Arrays to store the results
t_vals =[]
y_vals= []
y1_vals =[]

# Initial values
t_vals.append(t_ini)
y_vals.append(y_ini)
y1_vals.append(y1_ini)

# Applying Euler's method
for i in range(n):
    t = t_vals[i]
    y = y_vals[i]
    y1 = y1_vals[i]

    # Updating t
    t= t + h
    t_vals.append(t)
    

    # Updating y using Euler's method
    yy = y1 + h * f(t, y, y1)
    y= y + h * y1
    y_vals.append(y)
    y1_vals.append(yy)

# Calculating exact solution
t_exact = linspace(t_ini, t_fin, 1000)
y_exact = exact_solution(t_exact)

# Plotting the results
figure(figsize=(10, 6))
plot(t_vals, y_vals, label='Euler Method', color='blue')
plot(t_exact, y_exact, label='Exact Solution', color='red', linestyle='--')
title('Solution of second order differential equation \n Using Euler method')
xlabel(r"$t\rightarrow$")
ylabel(r"$y\rightarrow$")
legend()
grid(True)
show()
