import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(x, y):
    return np.vstack((y[1], -(2 * (y[1])**3 + y[0]**2 * y[1]) / np.cos(x)))

def boundary_conditions(ya, yb):
    return np.array([ya[0] - 2**(-1/4), yb[0] - (12**(1/4))/2])

#To define the initial mesh
x_mesh = np.linspace(np.pi/4, np.pi/3, 100)

# Initial guess for the solution
y_guess = np.zeros((2, x_mesh.size))

#To solve the BVP
sol = solve_bvp(ode, boundary_conditions, x_mesh, y_guess)

#To evaluate the solution at finer mesh for plotting
x_plot = np.linspace(np.pi/4, np.pi/3, 100)
y_plot = sol.sol(x_plot)[0]

#To plot the solution
plt.figure()
plt.plot(x_plot, y_plot, label='Numerical solution')
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'y$\rightarrow$')
plt.title(r"Solution to y''= $-(2(y')^{3}+ y^{2}y')sec(x)$")
plt.legend()
plt.grid(True)
plt.show()
