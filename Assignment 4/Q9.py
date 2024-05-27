from numpy import *
from matplotlib.pyplot import *
from scipy.stats import uniform

""" Density function defined form 3<x<7, a factor if 1/4 gives the normalization """
def density(x):
    return where((x > 3) & (x < 7), 1/4, 0) 

n = 10000
proposal_width = 1  # Width of the uniform proposal distribution
theta = []
theta.append(4)  # Initial state within the target range (3,7)

for i in range(n):
    # Proposes a new state from a uniform distribution centered at current_state
    theta_prime = theta[i] + random.uniform(-proposal_width, proposal_width)
    r = random.rand() #acceptance ratio

    # Updates theta
    if density(theta_prime) / density(theta[i]) > r:
        theta.append(theta_prime)
    else:
        theta.append(theta[i])

#Markov chain
figure(figsize=(10, 8))
subplot(2,1,1)

plot(theta, 'c-')
xlabel(r'Iteration')
ylabel(r'$\theta$')
title('Markov Chain')

figure(figsize=(10, 8))
subplot(2,1,2)

# Plots the histogram of the sampled values
hist(theta, bins=30, density=True, alpha=0.6, edgecolor='blue', label='Density Histogram')

# Plots the true density function
x = linspace(1, 9, 1000)
plot(x, density(x),'r-', label='True Density Function')
legend()
xlabel(r'$\theta$')
ylabel('Density')
title('Metropolis Method')
tight_layout()
show()
