import numpy as np


def inner_product(x,y):   #compute the inner product  given two vectors x and y
    if len(x)==len(y): #checks if the lengths of each vector align
        a = []
        for i in range(len(x)):
            a.append(x[i]*y[i])
        result = np.sum(a)
        return result
    else:
        return "error"

def proj(a,b):              #returns the projection of a onto b
    if inner_product(b,b) == 0:
        return b-b
    else:
        return (inner_product(a,b)/inner_product(b,b))*b

#THIS NEEDS SERIOUS WORK LOOOOL MAKE THIS BETTER
def random_independent_matrix(n, m):  #generates a random matrix with linearly independent columns
    A = np.random.randn(n, m)
    '''while True:
        A = np.random.randn(n, m)  # normal distribution
        if np.linalg.matrix_rank(A) == m:           #checks for linear independence (rank = m => linear independence)
            return A'''
    s = np.linalg.svd(A, full_matrices=True, compute_uv=True, hermitian=False)[1]
    s = np.diag(s)
    return s

def gram_schmidt(A):  #constructs a new matrix of basis vectors, where A's columns are an orthonormal basis themselves
    B = np.zeros_like(A, dtype = float)  #creates a 0 matrix of the same dimensions
    if len(A)!=len(B):
        return 'error'  #checks if the bases have the same dimension
    l_1, l_2 = len(A[0]), len(B[0])          #checks if the vectors in the bases have the same dimension (note:
                                             #bases do not always have the same dimension if zero values are not included;
                                             #however, this fixes the dimension of each basis to be equal
                                             #since this is not possible to do deterministically
    for vector in A:
        if len(vector) != l_1:
            return 'Error: Bll vectors in the basis must have the same dimension'
    for vector in B:
        if len(vector) != l_2:
            return 'Error: Bll vectors in the basis must have the same dimension'

    #check for orthogonality:
    C = np.zeros_like(A, dtype = float)  #create a matrix of inner products; this should be a zero matrix for a basis
    for i in range(len(A[:,0])):
        for j in range(len(A[:, 0])):
            C[i,j] = inner_product(A[:,i],A[:,j])
            C[i,i] = 0  #hand-wave, these diagonals should return non-zero values whilst everything else should be zero.
    if abs(C.any()) > 1e-12:
        print('The gram schmidt process only works when the basis is orthogonal; this basis will not return a valid'
              ' answer.')
        return 'Error'

    #the gram schmidt process:
    B[:, 0] = A[:, 0]
    for i in range(A.shape[1]):
        B[:,i] = A[:,i]
        for j in range(i):
            B[:,i] -= proj(A[:,i],B[:,j])
    return B


def normalise(A):
    if A == 'Error':
        return 'Error'
    v,factors = [], []
    for i in range(A.shape[1]):
        v.append(A[:,i])
        factors.append(np.sqrt(abs(inner_product(v[i],v[i]))))
        if factors[i] != 0:
            A[:,i] /= factors[i]
        else:
            print('Error - 0 vector detected; therefore not normalisable')
            pass
    return A

rng = np.random.default_rng(4)
n = rng.integers(low = 2, high = 10)
m = rng.integers(low = 2, high = 10)
A = random_independent_matrix(n, m)
C = gram_schmidt(A)
print(C)
Q = normalise(C) #for QA Decomposition
print(Q)
R = Q.T @ A
