import numpy as np

rng = np.random.default_rng(1)
n = rng.integers(low = 1, high = 50)
m = rng.integers(low = 1, high = 50)
A = rng.integers(-5, 5, size=(n,m))
A[A==0] = 1

#Doolittle algorithm for LU decompositon   #note, this algorithm cannot handle pivots being 0; this would need
                                           #a permuation matrix
def LU_Decomposition(A):
    n,m = A.shape
    if n >= m:
        L = np.eye(n,m)
    else:
        L = np.eye(n)
    U = A.copy().astype(float)
    #print('L_initial:', L, 'U_initial:', U)
    for i in range(min(n,m)):  #looping over the rows
        for j in range(i+1,n):   #looping over the rows under the pivot row
            factor = U[j,i]/U[i,i]
            L[j,i] = factor
            U[j,i:] = U[j,i:]-factor*U[i,i:]
            #print('L: ',i,',',j, L)   to see the algorithm at work unhashtag these
            #print('U: ',i,',',j, U)
    U = U[:m, :]
    return L,U
L,U = LU_Decomposition(A)

x = A - L@U

def total_error(A,L,U):     #computes the mean average error across the matrices (here due to floating point arithmetic)
    x = A - L @ U
    sums = []
    for i in range(len(x)):
        sums.append(np.sum(abs(x[i,:])))
    return np.sum(sums)/len(x)

L,U = LU_Decomposition(A)
print(x)   #allows user to inspect for outlying errors
print(total_error(A,L,U))
l = [len(A[i]) for i in range(len(A))]
print(l)
#print(A)