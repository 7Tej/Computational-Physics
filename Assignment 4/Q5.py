from numpy import *
from matplotlib.pyplot import *

n = 10000
#x1 and x2 are uniform deviates
x1 = random.rand(n)
x2 = random.rand(n)

y1 = sqrt(-2*log(x1))*cos(2*pi*x2)
y2 = sqrt(-2*log(x1))*sin(2*pi*x2)

random_no = concatenate((y1,y2))

#Hostogram plot of the generated random numbers
hist(random_no, bins = 23, density = True, edgecolor ='black', label = 'Density Histogram')

#Gaussian pdf
x = linspace(-5,5,1000)
pdf = (1/sqrt(2*pi))*exp(-0.5*x**2)
plot(x, pdf, 'r-', label='Gaussian pdf ')

title('Box Muller method for Gaussian PDF')
xlabel(r'Random numbers$\rightarrow$')
ylabel(r'Density$\rightarrow$')
legend()
