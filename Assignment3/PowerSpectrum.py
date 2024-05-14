from numpy import *
from matplotlib.pyplot import *
import numpy.random as rand
from scipy.stats import *


fxp = loadtxt('D:\\ONEDRIVE\\Documents\\noise.txt')
n = len(fxp)
p = arange(n)
fxmin = fxp[0]
fxmax = fxp[-1]
dfx = (fxmax - fxmin) / n

figure(figsize=(20, 15))

FT = fft.fft(fxp, norm='ortho')
Per = (abs(FT))**2

f = fft.fftfreq(n)
freq = 2 * pi * f


subplot(5, 3, 1)
scatter(p, fxp, label='Data points', color=rand.rand(3,))  
xlabel(r'$p$')
ylabel(r'$f(x_{p})$')
title(r'Independent Measurements of a Quantity vs Index')
legend()
grid()


subplot(5,3,2)
plot(freq,abs(FT),label='DFT')
legend()
ylabel(r'$|F(k_{q})|$')
xlabel(r'$k_{q}$')



subplot(5, 3, 3)

plot(freq, Per, label='Periodogram', color=rand.rand(3,))  
ylabel(r'$|F(k_{q})|^{2}$')
xlabel(r'$k_{q}$')
legend()
grid()


kq_min=min(freq)
kq_max=max(freq)
dk=(kq_max-kq_min)/len(freq)
"""Binning the frequencies"""

k=n//10
k_bin=linspace(kq_min,kq_max,11)
#print('k_bin',k_bin)
kvals = 0.5 * (k_bin[1:] + k_bin[:-1]) #mean frequency of each bin

"""Calculates the mean freqeuncy and mean power spectral density of each pin and appends their respective arrays"""

PS_mean=[]
for i in range(10):
    bin_i = where(logical_and(freq >= k_bin[i], freq < k_bin[i + 1]))
    #print(bin_i)
    bin_PS = Per[bin_i]
    #print(bin_PS)
    bin_mean = mean(bin_PS)
    #print('bin_mean',bin_mean)
    PS_mean.append(bin_mean)


subplot(5, 3, 4)

hist(kvals,k_bin,weights=PS_mean,color=rand.rand(3,),edgecolor='black',label='Binned Spectrum')

ylabel(r'$|F(k_{q})|^{2}$')
xlabel(r'$k_{q}$')
legend()

"""Here I am binned the sample and obtained the power spectrum of each pin"""


k = n // 10
Per=[]
Perr = []
F_bin = []


# Binning the data and the power spectrum into 10 k bins
for i in range(10):
    x_bin = fxp[i*k:(i+1)*k]
    FT_bin = fft.fft(x_bin, norm='ortho')
    Per_bin = (abs(FT_bin))**2
    Per.append(Per_bin)

    Per_bin_shifted = fft.fftshift(Per_bin)  # Shifts the binned periodogram
    f_bin = fft.fftfreq(k)
    freq_bin = fft.fftshift(fft.fftfreq(k)) * 2 * pi  # Shifts the frequencies

    F_bin.append(freq_bin)
    Perr.append(Per_bin_shifted)

    color = rand.rand(3,)  # Random color for each subplot
    subplot(5, 3, i+5)
    plot(freq_bin, Per_bin_shifted, label=f'PS of bin {i+1}', color=color)  # Plots the binned power spectrum 
    ylabel(r'$|F(k_{q})|^{2}$')
    xlabel(r'$k_{q}$')
    legend()
    grid()


#Flattens the arrays
F_bin_flat= concatenate(F_bin)
Per_flat = concatenate(Per)

subplot(5,3,15)
#Histogram plot
hist2d(F_bin_flat, Per_flat, bins=10,cmap='Blues')
xlabel(r'$k_{q}$')
ylabel(r'$|F(k_{q})|^{2}$')
title('2-D histogram of 10 k bins, \n where the sample is binned first', loc='right')


Bartlett = mean(Perr)  
print('Spectrum Estimate (Bartlett) =', Bartlett,'units of spectral density')  # Bartlett estimate of power spectrum

tight_layout()  
show()

"""This code has been revised after plots were attached to pdf"""
