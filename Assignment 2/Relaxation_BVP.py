import numpy as np
import matplotlib.pyplot as plt

g = 9.8
x0 = 0
x1 = 0
t1 = 10
N = 70
h = t1 / N
w = 1.1 #Relaxation parameter

def exact_sol(t,t1):
    return -0.5*g*t**2 + 0.5*t1*g*t

def f(t, x, v):
    dvdt = -g  # acceleration
    return dvdt
    
#defining the Successive Relaxation method
def SOR(f, t, x0, h, tol, w):
    x = np.zeros(len(t))
    x[0] = x0

    condition = True
    count = 0
    x_iterations = []

    while condition:
        err = 0
        for i in range(1, len(t) - 1):
            x_new = (1 - w) * x[i] + (w / 2) * (x[i - 1] + x[i + 1] - (h**2) * f(t[i], x[i], (x[i + 1] - x[i - 1]) / (2 * h)))
            err = max(err, abs(x_new - x[i]))
            x[i] = x_new
            count += 1
        x_iterations.append(np.copy(x))

        if err < tol:
            condition = False

    return x_iterations, count

t = np.arange(0, t1 + h, h)
x_iterations, iterations = SOR(f, t, x0, h, tol, w)
x= x_iterations[-1]

# Plotting the candidate solutions
plt.figure(figsize=(20, 12))
iterations_to_plot = [100, 200, 300, 400, 500, 750, 1000, len(x_iterations) // 2 ,len(x_iterations) // 2 + 50, len(x_iterations) // 2 + 500, len(x_iterations) - 1]

for idx in iterations_to_plot:
    plt.plot(t, x_iterations[idx], label=f'Iteration {idx + 1}')
plt.title(r' Relaxation Method for BVP', fontsize=20)

plt.plot(t, x, 'ro', markersize = 8, label='Numerical Solution')
plt.plot(t,exact_sol(t,t1),'b^', label = 'Exact Solution')

plt.xlabel(r't$\rightarrow$', fontsize=20)
plt.ylabel(r'x$\rightarrow$', fontsize=20)
plt.legend()
plt.grid(True)
plt.show()
print("Number of iterations:", iterations)
plt.tight_layout()
