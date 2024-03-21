import numpy as np
A = np.array([[5, -2],[-2, 8]])

def eigen_qr_simple(A, iterations=100):
    Ak = np.copy(A)
    n = A.shape[0]
    QQ = np.eye(n) #n*n identity matrix
    for k in range(iterations):
        Q, R = np.linalg.qr(Ak) #QR decomposition
        Ak = R @ Q
        QQ = QQ @ Q
        
        if k==99:
            print('Eigenvalues of A using QR decomposition=',np.diag(Ak))
            
            
    return Ak, QQ

# We call the function    
eigen_qr_simple(A)

# Eigenvals calculated using numpy module 
eigenvalues, eigenvectors = np.linalg.eigh(A)
print('Eigenvalues using numpy.linalg.eigh() =',eigenvalues)
