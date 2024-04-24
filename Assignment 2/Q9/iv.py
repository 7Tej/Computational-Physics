import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def ode(x, y):
    return np.vstack((y[1], 0.5 - (y[1])**2 / 2 - y[0] * np.sin(x) / 2))

def boundary_conditions(ya, yb):
    return np.array([ya[0] - 2, yb[0] - 2])

#To define the initial mesh
x_mesh = np.linspace(0, np.pi, 100)

# Initial guess for the solution
y_guess = np.zeros((2, x_mesh.size))

#To solve the BVP
sol = solve_bvp(ode, boundary_conditions, x_mesh, y_guess)

#To evaluate the solution at finer mesh for plotting
x_plot = np.linspace(0, np.pi, 100)
y_plot = sol.sol(x_plot)[0]

#To plot the solution
plt.figure()
plt.plot(x_plot, y_plot, label='Numerical solution')
plt.xlabel(r'x$\rightarrow$')
plt.ylabel(r'y$\rightarrow$')
plt.title(r"Solution t y''= $\frac{1}{2} - \frac{(y')^{2}}{2} - \frac{ysin(x)}{2}$")
plt.legend()
plt.grid(True)
plt.show()
