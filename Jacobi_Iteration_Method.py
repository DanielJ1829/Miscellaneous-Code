import numpy as np
from test_cases_gauss import unique_large
from GaussJordanElimination import get_solution_vector
#this code allows us to iteratively solve a system of equation Ax=b iteratively
#we have a requirement that the iteration matrix's spectral radius (i.e. the max absolute value of the eigenvalues)
#has to be less than one for this method to converge. We run this test in a different function to help catch errors
#the code is inefficient at places. This is because this code serves as a learning exercise, where
#code readability is most important


def decompose(A):
    """
    :param A: the square matrix to be decomposed
    :return: D - the diagonal matrix
    L - the lower triangular part of the matrix (w/o diagonal)
    U - the upper triangular part of the matrix (w/o diagonal)
    """
    if len(A)!=len(A[0]):
        return 'Matrix must be square'
    n = len(A)
    [D,L,U]= [np.zeros((n,n),dtype=float) for _ in range(3)]
    for i in range(n):
        D[i,i] = int(A[i,i])
    for i in range(n):
        for j in range(i+1,n):
            U[i,j] = int(A[i,j])
        for j in range(i):
            L[i,j] = int(A[i,j])
    return D,L,U

def check_convergence(D,L,U):
    """
    function that checks whether the spectral radius, the max eigenvalue of D_inv(L+U), is less than 1
    :returns: a True or False value and the inverse of D (for later)
    """
    #invert D (first principles)
    n = len(D)
    D_inv = np.zeros((n,n), dtype = float)
    for i in range(n):
        D_inv[i,i] = 1/D[i,i]
    if np.max(np.abs(np.linalg.eigvals(D_inv @ (L+U))))<1:
        return True
    else:
        return False

def JacobiIteration(A,b,iterations):
    """
    :param b: the right hand side of the matrix equation Ax=b
    :param iterations: the number of iterations
    :return: an approximation of the solution vector, x
    """
    D,L,U = decompose(A)
    if check_convergence(D,L,U) == False:
        return 'This Matrix does meet the criteria in which this method converges, so will not solve the system'
    n = len(A)
    m = len(b)
    if m!=n:
        return 'Error - Solution vector or matrix has incorrect dimensions'
    D_inv = np.zeros((n, n), dtype=float)
    for i in range(n):
        D_inv[i, i] = 1 / D[i, i]
    x_iter = np.zeros((iterations,m), dtype=float)
    x_iter[0] = np.zeros(m,float)
    for i in range(1,iterations):
        x_iter[i] = D_inv@(b-(L+U)@x_iter[i-1])
    return x_iter[-1]

A,b,name = unique_large(100,seed=0)
D,L,U = decompose(A)
converges = check_convergence(D,L,U)
a = JacobiIteration(A,b,100)
a_actual = np.linalg.inv(A)@b
errors = []
for i in range(len(a)):
    errors.append(float(abs(a[i]-a_actual[i])))
