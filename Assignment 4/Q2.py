from numpy import *
from matplotlib.pyplot import *
                            

# Generates 10,000 random numbers between 0 and 1
random_numbers = random.rand(10000)


hist(random_numbers, bins=50, density=True, alpha=0.6, color='pink', edgecolor='black')

# Uniform PDF
x = linspace(0, 1, 100)
uniform_pdf = [1] * len(x)  # Uniform PDF between 0 and 1 is a constant value of 1
plot(x, uniform_pdf, 'r--', linewidth=2)

title('Density Histogram of random.rand() Numbers vs Uniform PDF')
xlabel('Random Number')
ylabel('Density')
legend(['Uniform PDF', 'Numpy Generated Random Numbers'])
show()
