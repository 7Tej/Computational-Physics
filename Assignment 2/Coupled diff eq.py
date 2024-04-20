import numpy as np
import matplotlib.pyplot as plt

#  To implement the system of ordinary differential equations (ODEs)
def ode_system(u, t):
    #To unpack the variables
    u1, u2, u3 = u

    # Defining the ODEs
    du1dt = u1  +2*u2 - 2*u3 +np.exp(-t)
    du2dt = u2 + u3 -2*np.exp(-t)
    du3dt = u1 + 2*u2+ np.exp(-t)

    return [du1dt, du2dt, du3dt]

# -To implement the fourth-order Runge-Kutta (RK4) method for a system of ODEs
def rk4_system(ode_system, u0, t, h):
    k1 = np.array(ode_system(u0, t))
    k2 = np.array(ode_system(u0 + 0.5 * h * k1, t + 0.5 * h))
    k3 = np.array(ode_system(u0 + 0.5 * h * k2, t + 0.5 * h))
    k4 = np.array(ode_system(u0 + h * k3, t + h))
    return u0 + (h / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

# - To define initial conditions
u0 = [3, -1, 1]  # Initial values for u1, u2, u3

# - To define the range for x values
t0 = 0
tf = 1
h = 0.001  # Step size

# Number of steps
n_steps = int((tf - t0) / h)

# - To initialize arrays to store t and u values
t_values = np.linspace(t0, tf, n_steps)
u_values = np.zeros((n_steps, 3))  # 3 columns for u1, u2, u3

# -To implement the RK4 method to solve the system of ODEs
u = np.array(u0)
for i in range(n_steps):
    u_values[i] = u
    u = rk4_system(ode_system, u, t0 + i * h, h)

# - To plot the solutions
plt.plot(t_values, u_values[:, 0], label='u1')
plt.plot(t_values, u_values[:, 1], label='u2')
plt.plot(t_values, u_values[:, 2], label='u3')
plt.xlabel(r"t$\rightarrow$")
plt.ylabel(r"u$\rightarrow$")
plt.title('Solution of the Coupled Differential Equations')
plt.legend()
plt.grid(True)
plt.show()
