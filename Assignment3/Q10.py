from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import *

def f(x,y):
    return exp(-(x**2+y**2))

def analytical_solution(kx, ky):
    return 0.5 *exp(-0.25 * (kx**2 + ky**2))

xmin,ymin,xmax,ymax = -50, -50, 50, 50

n = 100  # Number of points in each dimension
dx = (xmax - xmin) / n
dy = (ymax - ymin) / n
x = linspace(xmin, xmax, n)
y = linspace(xmin, xmax, n)
X, Y = meshgrid(x, y)

Z = f(X, Y)

fourier_transform = fft.fftshift(fft.fft2(Z,norm='ortho'))

#Sampling the frequencies
kx = fft.fftshift(np.fft.fftfreq(n, dx))*2*pi
ky = fft.fftshift(np.fft.fftfreq(n, dy))*2*pi

phase_x = dx * sqrt(n / (2 * pi))*exp(-1j * kx * xmin)
phase_y = dy * sqrt(n / (2 * pi))*exp(-1j * ky * ymin)

FT= fourier_transform *phase_x*phase_y 

KX, KY = meshgrid(kx, ky)

fig = figure(figsize=(12, 6))
# Plots the analytical solution
ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(KX, KY, analytical_solution(KX, KY), cmap='viridis', alpha=0.5,)
ax1.set_title('Analytical Fourier Transform')
ax1.set_xlabel('$k_{x}$')
ax1.set_ylabel('$k_{y}$')
ax1.set_zlabel('$F(k_{x},k_{y})$')

# Plot the Absolute value of the Discrete Fourier transform
ax2 = fig.add_subplot(122, projection='3d')
surf2 = ax2.plot_surface(KX, KY, abs(FT), cmap='cool', alpha=0.5)
ax2.set_title('Discrete Fourier Transform')
ax2.set_xlabel('$k_{x}$')
ax2.set_ylabel('$k_{y}$')
ax2.set_zlabel('$FFT(k_{x},k_{y})$')

suptitle('Fourier transforms of 2-D Gaussian Function', fontsize=16)
