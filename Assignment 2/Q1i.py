import numpy as np
import matplotlib.pyplot as plt

#To Define the true solution function
def true_solution(x):
    return np.exp(1 - 9*x)

#To Define the implicit Euler method function
def implicit_euler(h, x_initial, x_final, y_initial):
    num_steps = int((x_final - x_initial) / h) + 1
    x_values = np.linspace(x_initial, x_final, num_steps)
    y_values = np.zeros(num_steps)
    y_values[0] = y_initial

    for i in range(1, num_steps):
        y_values[i] = y_values[i-1] / (1 + 9*h)

    return x_values, y_values

# Given initial conditions
x_initial = 0
x_final = 1
y_initial = np.exp(1)
h = 0.001

#To Calculate using implicit Euler method
x_values, y_values_approx = implicit_euler(h, x_initial, x_final, y_initial)

#To Calculate true solution
y_values_true = true_solution(x_values)

#To Print y values in an array
print("x values:", x_values)
print("Approximate y values:", y_values_approx)

#To Plot the results
plt.plot(x_values, y_values_approx, label='Implicit Euler Approximation')
plt.plot(x_values, y_values_true, label='True Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Implicit Euler Method vs. True Solution')
plt.legend()
plt.grid(True)
plt.show()
