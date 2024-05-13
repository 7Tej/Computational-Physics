import numpy as np
import matplotlib.pyplot as plt

def numerical_fourier_transform(func, k_values, xmin, xmax, n=1000):
    """
    Compute the Fourier Transform of a given function using numerical integration.

    Parameters:
        func: callable
            The function to be transformed.
        k_values: array_like
            Array of k values at which to evaluate the Fourier Transform.
        xmin: float
            The minimum value of x.
        xmax: float
            The maximum value of x.
        n: int, optional
            The number of sample points for numerical integration (default is 1000).

    Returns:
        array_like: Fourier Transform values corresponding to the k_values.
    """
    dx = (xmax - xmin) / n
    x_values = np.linspace(xmin, xmax, n, endpoint=False)
    result = np.zeros_like(k_values, dtype=np.complex128)
    for p in range(n):
        x = xmin + p * dx
        result += func(x) * np.exp(-1j * k_values * x) * dx * np.sqrt(n / (2 * np.pi))
    result *= np.sqrt(1 / n)
    return result

# Define the function
def function(x):
    return np.where((-1 < x) & (x < 1), 1, 0)

# Define the range of x values and k values
xmin = -5
xmax = 5
k_values = np.linspace(-10, 10, 1000)

# Compute Fourier Transform
FT = numerical_fourier_transform(function, k_values, xmin, xmax)

# Plot the absolute value of Fourier Transform
plt.plot(k_values, np.abs(FT))
plt.title('Absolute Value of Fourier Transform')
plt.xlabel('k')
plt.ylabel('|FT(k)|')
plt.grid(True)
plt.show()
