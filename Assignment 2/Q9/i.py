import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(x, y):
    return np.vstack((y[1], -np.exp(-2*y[0])))

def boundary_conditions(ya, yb):
    return np.array([ya[0] - 0, yb[0] - np.log(2)])

#To define the initial mesh
x_mesh = np.linspace(1, 2, 100)

# Initial guess for the solution
y_guess = np.zeros((2, x_mesh.size))

#To solve the BVP
sol = solve_bvp(ode, boundary_conditions, x_mesh, y_guess)

#To evaluate the solution at finer mesh for plotting
x_plot = np.linspace(1, 2, 100)
y_plot = sol.sol(x_plot)[0]

#To plot the solution
plt.figure()
plt.plot(x_plot, y_plot, label='Numerical solution')
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'y$\rightarrow$')
plt.title(r"Numerical solution to y'= $-e^{-2y}$")
plt.legend()
plt.grid(True)
plt.show()
