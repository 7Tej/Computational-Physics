"""Code for chi-squared test for rolling of two dice,
    observable is sum of numbers obtained in each roll:
    with given two sets of rolls"""
    
from numpy import *
import scipy.stats as stats

p = array([1/36, 1/18, 1/12, 1/9, 5/36, 1/6, 5/36, 1/9, 1/12, 1/18, 1/36])
Run_1 = array([4, 10, 10, 13, 20, 18, 18, 11, 13, 14, 13])
Run_2 = array([3, 7, 11, 15, 19, 24, 21, 17, 13, 9, 5])

n = sum(Run_1)

def chisq_stat(p,Run,n):
    V = sum(((Run - n*p)**2)/n*p)
    return V

chi1 = chisq_stat(p,Run_1,n)
chi2 = chisq_stat(p,Run_2,n)

print('V1 =', chi1)
print('V2 =', chi2)

#dof
k = 11-1
    
p1 = 1- stats.chi2.cdf(chi1,df = k)
p2 = 1- stats.chi2.cdf(chi2,df = k)

def chi_sq_test(P):
    
    if (P <0.01) or (P>0.99):
        print('not sufficiently random')
    elif (0.01<= P <= 0.05) or (0.95<= P <= 0.99):
        print('suspect')
    elif (0.05<= P <= 0.10) or (0.90<= P <= 0.95):
        print('almost suspect')
    else:
        print('sufficiently random')

""" For Run 1"""
print('For Run 1')
chi_sq_test(p1)

""" For Run 2"""
print('For Run 2')
chi_sq_test(p2)
