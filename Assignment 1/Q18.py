import numpy as np

def __find_p(x):
    return np.argwhere(np.isclose(np.abs(x), np.linalg.norm(x, np.inf))).min()

def __iterate(A, x, p):
    
    y = np.dot(A, x)       
    μ = y[p]      
    p = __find_p(y)     
    error = np.linalg.norm(x - y / y[p],  np.inf)
    x = y / y[p]
    
    return (error, p, μ, x) 

def power_method(A, tolerance=1e-3, max_iterations=10000):
    
    n = A.shape[0]
    x = np.ones(n)
    
    p = __find_p(x)
    
    error = 1
    
    x = x / x[p]
    
    for _ in range(max_iterations):
        
        if error < tolerance:
            break
            
        error, p, μ, x = __iterate(A, x, p)
        
    
    print('Dominant eigenvalue using Power Method =',μ)

def accuracy(a,b):
    i= abs(((a-b)/b)*100)
    print('accuracy=',i,'%')
   

A=np.array([[2, -1, 0], [-1, 2, -1],[0, -1, 2]])
eigenvalues= np.linalg.eigvals(A)
μ_= np.max(np.abs(eigenvalues))
power_method(A)
print('Actual dominant eigval=',μ_)
