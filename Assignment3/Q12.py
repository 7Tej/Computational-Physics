from numpy import *
from matplotlib.pyplot import *
def g(x):
    return exp(-x**2)

def h(x):
    return exp(-4*x**2)
    
def f(x):
    return sqrt(pi/5)*exp(-4*(x**2)/5)

#Sampling
xmin = -50
xmax = 50
n = 1600

dx = (xmax - xmin) / n
xp= arange(xmin, xmax, dx)

FT_g=fft.fft(g(xp),norm= 'ortho')
FT_h=fft.fft(h(xp),norm= 'ortho')

#Sampling the frequencies
freq = fft.fftfreq(n, d=dx)
kq=2*pi*freq

phase = dx * sqrt(n / (2 * pi))*exp(-1j * kq * xmin)

#Adjusts the normalization
FFT_g = phase*FT_g
FFT_h = phase*FT_h

#Product of the DFTs
FFT_gh = FFT_g*FFT_h

#Calculates the inverse fourier transform of the produc
func = fft.fftshift(fft.ifft(FFT_gh, norm='ortho'))

#Gives the convolution function
conv= func* dx* sqrt(n)

#figure(figsize=(25,50))
plot(xp, g(xp), label='g(x) = exp(-x^2)')
plot(xp, h(xp), label='h(x) = exp(-4x^2)')
plot(xp, conv,label='numerical convolution')
plot(xp,f(xp),label='analytical convolution')
title('Plot of Numerical Convoluion using DFT \n with Analytical convolution')
xlim(-10,10)

xlabel(r'$x_{p}$')
ylabel(r'$function(x_{p})$')
grid()
legend()
show()








