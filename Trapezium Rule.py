import numpy as np
#insert function here
from scipy import integrate

function = lambda x: np.log(x)
def trapezoidal(function, a, b, error):
    """
    :param function: the function you'd like to approximate the integral result for
    :param a: the lower bound of the integral
    :param b: the upper bound of the integral
    :param error: the desired error to
    :returns: the numerical approximation
    """
    print('n \t\t ea  \t\t et \t\t integral \t\t result')
    result, ea = integrate.quad(function, a, b)
    ea, old, n = 100, 100, 1
    while ea > error:
        h = (b-a)/n
        sum = 0
        for i in range(1,n):
            sum += function(a+i*h)
        integral = (h/2)*(function(a)+2*sum+function(b))
        ea = abs((integral-old)/integral)*100  #approximate error
        et = abs((result - integral)/result)*100 #the actual error
        print(f"{n:<8.4g} {ea:<11.5g} {et:<11.5g} {integral:<15.6g} {result:<12.6g}")
        old = integral
        n+=1
    return integral, ea, n
integral, error, n = trapezoidal(function, 2, 4, 0.001)
print('result after {} iterations: {:.6f}'.format(n, integral))
print('total error: {:.6f}'.format(error))

#note this is for a specific integration between 2 and for for a log(x) integral