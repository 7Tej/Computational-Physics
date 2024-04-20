from numpy import *
from scipy.integrate import solve_ivp
from matplotlib.pyplot import *
from scipy.optimize import*

g = 9.8
x0 = 0
t1 = 10

def f(t, r):
    x, v = r
    dxdt = v  # velocity
    dvdt = -g  # acceleration

    return dxdt, dvdt

@vectorize
def shooting(v0):
    sol = solve_ivp(f, (t[0], t[-1]), (x0, v0), t_eval=t)
    x, v = sol.y
    return x[-1]

def plot_func(v0):
    sol = solve_ivp(f, (t[0], t[-1]), (x0, v0), t_eval=t)
    x, v = sol.y
    return x

def exact_sol(t,t1):
    return -0.5*g*t**2 + 0.5*t1*g*t

v_guess = linspace(40,50,20)
labels = [f"x'(0)={v0:.3f}" for v0 in v_guess]

t = linspace(0, t1, 50)
diff=[]
fig, ax = subplots(figsize=(14, 14))
for v0, label in zip(v_guess, labels):
    
    d = [abs(plot_func(v0)[-1] - 0)]
    diff.append(d)
    
    plot(t, plot_func(v0), label=label)
    ylim(0,150)
    xlim(0,11)
    v_ = newton(shooting, v0)
    num_sol = solve_ivp(f, (0, t1), (x0, v_), t_eval=t)
    x, v = num_sol.y
   
i = argmin(diff) 
print(i)

num_sol1 = solve_ivp(f, (0, t1), (x0, v_guess[i]), t_eval=t)
x_, v = num_sol1.y
plot(t, x_, 'm:',label='Numerical Solution: Using argmin')

plot(t, x, 'ro',label='Numerical Solution: Using Newtons method') 
plot(t,exact_sol(t,t1),'g-', label = 'Exact Solution')
title("Plot for Shooting Method with Candidate Solutions", fontsize =20)
xlabel(r"t$\rightarrow$", fontsize =20)
ylabel(r"x$\rightarrow$", fontsize =20)
grid()
tight_layout()  
legend()
