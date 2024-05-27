from numpy import *
import emcee 
import corner
from matplotlib.pyplot import *

x = []
y = []
yerr = []

with open("D:\\emcee_data.txt", 'r') as file:
    next(file)  # Skip the header row
    for line in file:
        columns = line.split()
        try:
            xi = int(columns[1])
            yi = int(columns[2])
            yerri = int(columns[3])
            x.append(xi)
            y.append(yi)
            yerr.append(yerri)
        except (IndexError, ValueError):
            pass

x= array(x)
y= array(y)
yerr= array(yerr)
print("x =", x)
print("y =", y)
print("yerr =",yerr)

# Model
def model(x,a,b,c):
    return a*x**2 + b*x +c

#Log Likelihood Function
def log_likelihood(theta, x, y, yerr):
    a,b,c = theta
    model_y = model(x,a,b,c)
    sigma2 = yerr**2

    #actually negative
    return 0.5*sum((y-model_y)**2/sigma2 + log(2*pi*sigma2))

#We are aprior uninformed about the parameters
#Thus, choosing an uniform prior 
def log_prior(theta):
    a, b, c = theta
    if -500 < a < 500 and -500 < b < 500 and 0 < c < 1000:
        return 0.0
    return -np.inf

#Posterior pdf
def log_probability(theta, x, y, yerr):
    lp = log_prior(theta)
    if not isfinite(lp):
        return -inf
    return lp - log_likelihood(theta, x, y, yerr) 

"""lp - log_likelihood because our defined loglikelihood is negative of the actual
    loglikelihood, if defined is the true one, we use lp + log_likelihood"""

#50 Markov chains
#Intial guess of parameters

from scipy.optimize import minimize
guess = (1,1,1)
soln = minimize(log_likelihood,guess, args=(x,y,yerr))   

#initialize Markov chain near the optimum reported minimized function

ndim = 3 #number of parameters
nwalkers = 50
nsteps = 4000

pos = soln.x + 1e-4*random.randn(nwalkers, ndim)

#using emcee library

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(x, y, yerr))
sampler.run_mcmc(pos, 4000)
samples = sampler.get_chain()

labels = [r"$a$", r"$b$", r"$c$"]
#Plotting the chains
figure(figsize=(10, 8))
for i in range(ndim):
    subplot(ndim, 1, i + 1)
    plot(samples[:, :, i], color='k', alpha=0.3)
    ylabel(labels[i])
xlabel('Step')
tight_layout()
show()

#Using corner library to plot the posterior pdf

# Extracting the best-fit values and uncertainties
flat_samples = sampler.get_chain(discard=100, thin=15, flat=True)
a_median = median(flat_samples[:, 0])
b_median = median(flat_samples[:, 1])
c_median = median(flat_samples[:, 2])
a_sigma = std(flat_samples[:, 0])
b_sigma = std(flat_samples[:, 1])
c_sigma = std(flat_samples[:, 2])

print("Best-fit values:")
print(f"a = {a_median:.3f} +/- {a_sigma:.3f}")
print(f"b = {b_median:.3f} +/- {b_sigma:.3f}")
print(f"c = {c_median:.3f} +/- {c_sigma:.3f}")

#Corner plots

fig = corner.corner(flat_samples, labels=labels, truths=[a_median, b_median, c_median])
show()


x_fit = linspace(min(x), max(x), 1000)
figure(figsize=(8, 8))
subplot (2,1,1)

# Plotting the data with best-fit model and 200 randomly chosen models from posterior
errorbar(x, y, yerr=yerr, fmt="o", color="k", label="Data")
plot(x_fit, model(x_fit, a_median, b_median, c_median), color="red", label="Best-fit model")
xlabel("x_fitted")
ylabel("y_fitted")
legend()
show()

figure(figsize=(8, 8))
subplot(2,1,2)
for _ in range(200):
    inds = random.randint(len(flat_samples), size=1)
    sample = flat_samples[inds, :]
    plot(x_fit, model(x_fit, sample[0, 0], sample[0, 1], sample[0, 2]), color="yellow", alpha=0.1)
xlabel("x_fitted")
ylabel("y_fitted")
errorbar(x, y, yerr=yerr, fmt="o", color="k", label="Data")
plot(x_fit, model(x_fit, a_median, b_median, c_median), color="red", label="Best-fit model", alpha =1)

legend()
show()
