#To find FFT uisng DFT of sinc function and plot the analytical & numerical Fourier Transforms
from numpy import *
from matplotlib.pyplot import *

#Sinc function
def f(x):
    return where(x == 0, 1, sin(x) / x)
    
        
#Normalized Analytical Fourier Transform        
def ft(k):
    return 0.5*sqrt(pi/2)* (sign(1 - k) + sign(1 + k))
    
    
#Sampling
xmin = -50
xmax = 50
n = 256
dx = (xmax - xmin) / n

xp= arange(xmin, xmax, dx)

#Calculating the analytical transform
y= f(xp)

# Computes the unitary & normalized Fourier transform
FT = fft.fft(y, norm='ortho')

#Sampling the frequencies
freq = fft.fftfreq(n, d=dx)
kq=2*pi*freq


phase = dx * sqrt(n / (2 * pi))*exp(-1j * kq * xmin)

FFT= phase*FT

figure(figsize=(8,6))
subplot(2,1,2)
plot(kq, real(FFT) , label='Numerical FT')

plot(kq, ft(kq),'r--', label='Analytical FT')
xlabel(r'$k_{q}$')
ylabel(r'$F(k_{q})$')
title('Fourier Tranforms(FT)')
grid(True)
legend()

figure(figsize=(8,6))
subplot(2,1,1)
plot(xp,f(xp),'c.-',label='sinc func')
xlabel(r'$x_{p}$')
ylabel(r'$f(x_{p})$')
title(r'$f(x)=\frac{sin(x)}{x}$')
grid(True)
legend()
tight_layout()
show()
