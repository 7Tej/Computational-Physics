#Relaxation (SOR)

# Defining equations to be solved
# in diagonally dominant form

f1 = lambda x,y,z,v,u: (1-0.1*y-z-v)/0.2
f2 = lambda x,y,z,v,u: (2-0.1*x+z-v+u)/4
f3 = lambda x,y,z,v,u: (3-x+y+2*u)/60
f4 = lambda x,y,z,v,u: (4-x-y-4*u)/8
f5 = lambda x,y,z,v,u: (5+y+2*z-4*v)/700

x_sol = 7.859713071
y_sol = 0.422926408
z_sol = -0.073592239
v_sol = -0.540643016
u_sol = 0.010626163

X1=[x_sol,y_sol,z_sol,v_sol,u_sol]

#Euclidean norm
def modulus(lst):
    s= sum(i**2 for i in lst)
    return s**0.5

# Initial setup
x0 = 0
y0 = 0
z0 = 0
v0 = 0
u0 = 0
count = 1

# Reading tolerable error
e = 0.01

# Reading relaxation factor
w = 1.25

# Implementation of successive relaxation


condition = True

while condition:
    x1 = (1-w) * x0 + w * f1(x0,y0,z0,v0,u0)
    y1 = (1-w) * y0 + w * f2(x1,y0,z0,v0,u0)
    z1 = (1-w) * z0 + w * f3(x1,y1,z0,v0,u0)
    v1 = (1-w) * v0 + w * f4(x1,y1,z1,v0,u0)
    u1 = (1-w) * u0 + w * f5(x1,y1,z1,v1,u0)
    
    X2=[x1, y1, z1, v1, u1]
    print('Diff in Euclidean norm of Approximate & True Solution vectors =',abs(modulus(X2)-modulus(X1)))
    print('%d) x1= %0.9f, x2= %0.9f, x3= %0.9f, x4= %0.9f and x5= %0.9f\n' %(count, x1,y1,z1,v1,u1))
    
   
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1
    v0 = v1
    u0 = u1

    condition = abs(modulus(X2)-modulus(X1))>e

print('\nSolution: Iteration number=%d, x1=%0.9f, x2=%0.9f, x3 = %0.9f, x4 = %0.9f and x5 = %0.9f\n'% (count-1,x1,y1,z1,v1,u1))
