import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def exact(x):
    return np.exp(sin(x))
def ode(x, y):
    return np.vstack((y[1], y[1] * np.cos(x) - y[0] * np.log(np.maximum(y[0], 1e-10))))

def boundary_conditions(ya, yb):
    return np.array([ya[0] - 1, yb[0] - np.exp(1)])

# To define the initial mesh
x_mesh = np.linspace(0, np.pi/2, 100)

# Initial guess for the solution
y_guess = np.zeros((2, x_mesh.size))

#To solve the BVP
sol = solve_bvp(ode, boundary_conditions, x_mesh, y_guess)

#To evaluate the solution at finer mesh for plotting
x_plot = np.linspace(0, np.pi/2, 100)
y_plot = sol.sol(x_plot)[0]

#To plot the solution
plt.figure()
plt.plot(x_plot, y_plot, label='Numerical solution')
plt.plot(x_plot, exact(x_plot),'r:', label='Exact solution')
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'y$\rightarrow$')
plt.title(r" Solution to y'' = y'cos(x) - yln(y)")
plt.legend()
plt.grid(True)
plt.show()
