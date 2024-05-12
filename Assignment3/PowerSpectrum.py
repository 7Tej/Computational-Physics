from numpy import *
from matplotlib.pyplot import *
import numpy.random as rand

fxp = loadtxt('D:\\ONEDRIVE\\Documents\\noise.txt')
n = len(fxp)
p = arange(n)
fxmin = fxp[0]
fxmax = fxp[-1]
dfx = (fxmax - fxmin) / n

figure(figsize=(10, 30))

FT = fft.fft(fxp, norm='ortho')
Per = (abs(FT))**2

f = fft.fftfreq(n)
freq = 2 * pi * f

subplot(12, 1, 1)
scatter(p, fxp, label='Data points', color=rand.rand(3,))  # Random color for scatter plot
xlabel(r'$p$')
ylabel(r'$f(x_{p})$')
title(r'Independent Measurements of a Quantity vs Index')
legend()
grid()

subplot(12, 1, 2)
plot(freq, Per, label='Periodogram', color=rand.rand(3,))  # Random color for line plot
ylabel(r'$|F(k_{q})|^{2}$')
xlabel(r'$k_{q}$')
legend()
grid()

k = n // 10
Perr = []
F_bin = []

# Binning the data and the power spectrum into 10 k bins
for i in range(10):
    x_bin = fxp[i*k:(i+1)*k]
    FT_bin = fft.fft(x_bin, norm='ortho')
    Per_bin = (abs(FT_bin))**2

    Per_bin_shifted = fft.fftshift(Per_bin)  # Shifts the binned periodogram
    f_bin = fft.fftfreq(k)
    freq_bin = fft.fftshift(fft.fftfreq(k)) * 2 * pi  # Shifts the frequencies

    F_bin.append(freq_bin)
    Perr.append(Per_bin_shifted)

    color = rand.rand(3,)  # Random color for each subplot
    subplot(12, 1, i+3)
    plot(freq_bin, Per_bin_shifted, label=f'PS of bin {i+1}', color=color)  # Plots the binned power spectrum 
    ylabel(r'$|F(k_{q})|^{2}$')
    xlabel(r'$k_{q}$')
    legend()
    grid()

Bartlett = mean(Perr)  
print('Spectrum Estimate (Bartlett) =', Bartlett,'units of spectral density')  # Bartlett estimate of power spectrum

tight_layout()  
show()
