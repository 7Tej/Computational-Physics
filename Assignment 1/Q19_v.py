from timeit import default_timer as timer
import numpy as np

# Defining matrix
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])


AAT=np.dot(A,np.transpose(A))
ATA=np.dot(np.transpose(A),A)

start = timer()
# To Perform Singular Value Decomposition (SVD)
# U, S, and VT are the left orhtogonal, Diagonal, and right orthogonal matrices respectively
U, S, VT = np.linalg.svd(A)

end = timer()

Eig= np.linalg.eigvals(AAT)
Eig_=np.linalg.eigvals(ATA)
print('Eigenvalues of AAT=',Eig)
print('Eigenvalues of ATA=',Eig_)

print("U (left singular vectors):\n", U)
print("S (singular values):\n", S)
print("VT (right singular vectors):\n", VT)

E= S**2
print('Eigvals of ATA if SVD is correct=',S**2)

print('Computation time=',end - start,'seconds')
