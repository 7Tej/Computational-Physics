import numpy as np
import matplotlib.pyplot as plt

# Euler's method function
def euler_method(f, t_values, y_initial, h):
    num_steps = len(t_values)
    y_values = np.zeros(num_steps)
    y_values[0] = y_initial

    for i in range(1, num_steps):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])

    return y_values

# To Define the function f(t, y) = y/t - (y/t)^2
def f(t, y):
    return y / t - (y / t) ** 2

# To Define the true solution y(t) = t / (1 + ln(t))
def true_solution(t):
    return t / (1 + np.log(t))

# Parameters
t_initial = 1
t_final = 2
y_initial = 1
h = 0.1

#To Generate t values
t_values = np.arange(t_initial, t_final + h, h)

# Euler's method
euler_values = euler_method(f, t_values, y_initial, h)

# True solution
true_values = true_solution(t_values)

#To Calculate absolute and relative errors
absolute_error = np.abs(euler_values - true_values)
relative_error = absolute_error / true_values

#To Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_values, euler_values, label="Euler's Method", marker='o')
plt.plot(t_values, true_values, label="True Solution", linestyle='--')
plt.title("Euler's Method vs True Solution")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()

#To Print errors
print("Absolute Error:")
print(absolute_error)
print("\nRelative Error:")
print(relative_error)
