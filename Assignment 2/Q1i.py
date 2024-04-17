import numpy as np
import matplotlib.pyplot as plt

# Defining the ODE function
def f(x, y):
    return -9 * y

# True solution function
def true_solution(x):
    return np.exp(1 - 9 * x)

# Implicit Euler method
def implicit_euler(f, y0, x0, xn, h):
    num_steps = int((xn - x0) / h) + 1
    x_values = np.linspace(x0, xn, num_steps)
    y_values = np.zeros_like(x_values)
    y_values[0] = y0

    for i in range(1, num_steps):
        y_values[i] = y_values[i - 1] / (1 + 9 * h)

    return x_values, y_values

# Defining initial conditions and step size
x0, xn = 0, 1
y0 = np.exp(1)
h = 0.001  # Step size

# To Solve using implicit Euler method
x_values, y_values = implicit_euler(f, y0, x0, xn, h)

#To Calculate true solution
true_y_values = true_solution(x_values)

#To Plot results
plt.plot(x_values, y_values, label='Implicit Euler')
plt.plot(x_values, true_y_values, label='True Solution', linestyle='--')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Implicit Euler Method vs True Solution')
plt.legend()
plt.grid(True)
plt.show()
