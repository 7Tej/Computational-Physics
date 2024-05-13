from numpy import *
import time
from matplotlib.pyplot import *


# Defining function that computes DFT using numpy.fft.fft
def nfft(num):
    return fft.fft(num, norm='ortho')

def DFT(num):
    n = len(num)
    p = arange(n)
    q = p.reshape((n, 1))
    fact = exp(-1j * 2 * pi * p * q / n)
    return dot(fact, num) / sqrt(n)





# Defining function that measures time taken by each method for different values of n
def calctime(n_values):
    DFT_times = []
    nfft_times = []
    for n in n_values:
        numbers = random.rand(n)  # Random number generator is used to generate n numbers
        start_time = time.time()
        DFT(numbers)

        DFT_t = time.time() - start_time
        DFT_times.append(DFT_t)

        ti = time.time()
        nfft(numbers)
        nfft_time = time.time() - ti
        nfft_times.append(nfft_time)

    return DFT_times, nfft_times


# Range of values for n
n_val = range(4, 101)

DFT_t, nfft_time = calctime(n_val)

# Plotting
plot(n_val,DFT_t , label='Manual DFT')
plot(n_val, nfft_time, label='Numpy FFT via DFT')
xlabel('Number of elements (n)')
ylabel(r'Time taken to compute DFT (seconds)')
title(r'Manual DFT vs Numpy FFT')
legend()
grid()
show()
