#Conjugate-Gradient Method

import numpy as np

#Euclidean Norm
def modulus(arr):
    s = 0
    for num in arr:
        s += num ** 2
    return s**0.5

x_sol = 7.859713071
y_sol = 0.422926408
z_sol = -0.073592239
v_sol = -0.540643016
u_sol = 0.010626163

X1=np.array([x_sol,y_sol,z_sol,v_sol,u_sol])
X1_mod=modulus(X1)

#Tolerance
e= 0.01


def conjgrad(A, b, x):
    
    r = b - np.dot(A, x)
    
    #search direction
    d = r
    r_mod = np.dot(np.transpose(r), r)
    
    for i in range(len(b)):
        Ad = np.dot(A, d)
        alpha = r_mod / np.dot(np.transpose(d), Ad)
        x = x + np.dot(alpha, d)
        r = r - np.dot(alpha, Ad)
        r_ = np.dot(np.transpose(r), r)
        
        X_mod= modulus(x)
        diff =abs(X_mod-X1_mod)
        print('\nDiff in Euclidean norm of Approximate & True Solution vectors =',diff)
        
        if diff<e:
            break
        d = r + (r_/r_mod)*d
        r_mod = r_
        print(i+1,')',x)
    print('\nSolution: Iteration number = ',i+1) 
    print('\nx1=', x[0],'x2=', x[1],'x3=',x[2],'x4=', x[3],'x5=',x[4])
    return x
    


A_= np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
x_= np.array([1,0,0,0,0])
b_=np.array([1,2,3,4,5])
conjgrad(A_,b_,x_)
    
