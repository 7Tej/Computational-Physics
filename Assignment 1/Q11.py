from numpy import *
A1= array([[3, -1, 1], [3, 6, 2], [3, 3, 7]])
b1= array([1, 0, 4])

A2=array([[10, -1, 0], [-1, 10, -2], [0, -2, 10]])
b2=array([9, 7, 6])

A3=array([[10, 5, 0, 0], [5, 10, -4, 0], [0, -4, 8, -1], [0, 0, -1, 5]])
b3=array([6, 25, -11, -11])

A4=array([[4, 1, 1, 0 ,1], [-1, -3, 1, 1, 0], [2, 1, 5, -1, -1], [-1, -1, -1, 4, 0],[0, 2, -1, 1, 4]])
b4=array([6, 6, 6, 6, 6])

A= array([A1,A2,A3,A4],dtype=object)
B= array([b1, b2, b3, b4],dtype=object)

for i in range(4):
    sol= linalg.solve(A[i],B[i])
    print('solution for set',i+1,'of linear equations',sol)
    #the ith element of the solution matrix represents to xi th solution
solution for set 1 of linear equations [ 0.03508772 -0.23684211  0.65789474]
solution for set 2 of linear equations [0.99578947 0.95789474 0.79157895]
solution for set 3 of linear equations [-0.79764706  2.79529412 -0.25882353 -2.25176471]
solution for set 4 of linear equations [ 0.78663239 -1.00257069  1.86632391  1.9125964   1.98971722]
