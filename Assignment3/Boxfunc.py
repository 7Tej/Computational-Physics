from numpy import *
from matplotlib.pyplot import *

# Sampling
xmin = -20
xmax = 20
n = 1000
dx = (xmax - xmin) / n
xp = linspace(xmin, xmax, n)

def g(x):
    return where(logical_and(-1 < x, x < 1), 1, 0)

#Analytical convolution function
def conv_ana(y):
    return where((0 <= y) & (y <= 2), 2 - y, where((-2 < y) & (y <= 0), 2 + y, 0))

#Convolution of box function with itself using DFT
def convolution(g):
    FT_g = fft.fft(g)
    c = fft.ifft(FT_g**2).real
    return c

g_padded = pad(g(xp), (0, n), 'constant', constant_values=(0, 0))
conv_num = convolution(g_padded) * dx

# Gives the convolution function
conv = conv_num[n // 2:3 * n // 2] 

figure(figsize=(10, 10))
xlim(-5, 5)
plot(xp, g(xp), label='f(x) = box function')
plot(xp, conv, '.-', label='numerical convolution')
plot(xp, conv_ana(xp),'b-', label = 'Analytical convolution')
title('Convolution of Box function with itself')
xlabel(r'$x_{p}$')
ylabel(r'$function(x_{p})$')
grid()
legend()
show()
