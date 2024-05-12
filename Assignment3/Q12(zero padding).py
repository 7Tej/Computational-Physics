from numpy import *
from matplotlib.pyplot import *
# Sampling
xmin = -20
xmax = 20
n = 1000
dx = (xmax - xmin) / n
xp= linspace(xmin,xmax,n)



def g(x):
    return exp(-x**2)
def h(x):
    return exp(-4*(x**2))

def f(x):
    return sqrt(pi/5)*exp(-4*(x**2)/5)

def convolution(g,h):
    FT_g=fft.fft(g)
    FT_h=fft.fft(h)
    FT_gh= FT_g*FT_h
    c=fft.ifft(FT_gh).real
    return c
    
g = pad(g(xp), (0,n), 'constant', constant_values=(0, 0))
h = pad(h(xp), (0,n), 'constant', constant_values=(0, 0))

conv_num = convolution(g, h)*dx



# Gives the convolution function
conv = conv_num[n//2:3*n//2] 

figure(figsize=(10,10))
xlim(-5,5)
plot(xp, g_func(xp), label='g(x) = exp(-x^2)')
plot(xp, h_func(xp), label='h(x) = exp(-4x^2)')
plot(xp, conv, 'r.-',label='numerical convolution')
plot(xp, f(xp), label='analytical convolution')
title('Plot of Numerical Convolution using DFT \n with Analytical Convolution')
xlabel(r'$x_{p}$')
ylabel(r'$function(x_{p})$')
grid()
legend()
show()
