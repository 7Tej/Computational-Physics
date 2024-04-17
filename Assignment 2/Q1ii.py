import numpy as np
import matplotlib.pyplot as plt

# To Define the function f(x, y) = -20(y-x)^2 + 2x
def f(x, y):
    return -20 * (y - x)**2 + 2 * x

# Parameters
x_initial = 0
x_final = 1
y_initial = 1/3
h = 0.01  # Step size

# Number of steps
num_steps = int((x_final - x_initial) / h)

# Arrays to store the results
x_values = np.zeros(num_steps + 1)
y_values = np.zeros(num_steps + 1)

# Initial values
x_values[0] = x_initial
y_values[0] = y_initial

#To Apply implicit Euler method
for i in range(num_steps):
    x = x_values[i]
    y = y_values[i]

    # Update x
    x_values[i + 1] = x + h

    # To Use Newton's method to solve for y_{n+1}
    # Initial guess for y_{n+1}
    y_next = y

    # Newton's method of iterations
    for _ in range(10):  # Using 10 iterations, could be adjusted based on desired precision
        y_next = y + h * f(x + h, y_next)
        # The derivative of f(x, y) with respect to y is -40(y-x), so we use this value for the Jacobian
        y_next -= (y_next - y - h * f(x + h, y_next)) / (-40 * (y_next - x))

    # Update y_{n+1}
    y_values[i + 1] = y_next

# To Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Implicit Euler Method', color='blue')
plt.title("Implicit Euler Method Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
