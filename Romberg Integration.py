import numpy as np
from scipy import integrate
#this code uses romberg integration to find accurate estimates of integrals of functions

#function:
f = lambda x: np.e**x
#integration limits:
a,b = 0, 1
#accurate integral value:
result, _ = integrate.quad(f,a,b)
#matrix size:
m = 5

#Trapezoidal function:
def trap(n,a,b,f):
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    fx = f(x)
    return (h/2)*(fx[0]+fx[-1]+2*np.sum(fx[1:-1]))

#Initialise values:
#matrix
def romberg_integration(m,a,b,f):
    """
    :param function: the function being integrated
    :param m: the number of iterations of richardson extrapolation
    :param a: the lower integration bound
    :param b: the upper integration bound
    :return: an approximation for the integral
    """
    I = np.zeros((m,m))  #an mxm matrix for 10 applications of Romberg Integration
    n = 2
    for i in range(m):
        I[i,0] = trap(n**i,a,b,function)
    for i in range(1,m):
        for k in range(1,i+1):
            I[i,k] = (4**(k)*I[i,k-1]-I[i-1,k-1])/(4**(k)-1)
    return I[-1,-1]

