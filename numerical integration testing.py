import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import integrate

def composite_trapezoid(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f(x)
    return (h/2) * (fx[0] + 2*np.sum(fx[1:-1]) + fx[-1])  #sums the boundary terms + 2*(all the other terms)

def composite_simpson(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("Simpson's rule requires even n")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f(x)
    S = fx[0] + fx[-1] + 4*np.sum(fx[1:-1:2]) + 2*np.sum(fx[2:-1:2]) #sums boundary terms then 4*odd & 2*even terms
    #(see derivation of Simpsons' 1/3 rule)
    return (h/3) * S

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
        I[i,0] = composite_trapezoid(f,a,b,n**i)
    for i in range(1,m):
        for k in range(1,i+1):
            I[i,k] = (4**(k)*I[i,k-1]-I[i-1,k-1])/(4**(k)-1)
    return I[-1,-1]

def convergence_study(f, a, b, ns):
    """
    :param f: the function being studied
    :param a: lower bound
    :param b: upper bound
    :param ns: the number of divisions/gridpoints in the interval; ns is a list of integers in powers of 2 ([2,4,8,...])
    :return: true_val - an accurate integration of the result, np.array.traps -
    """
    true_val, _ = integrate.quad(lambda t: f(np.array([t]))[0] if isinstance(f(np.array([t])), np.ndarray) else f(t), a, b)
    traps = []  #array for the trapezium approximations
    simps = []  #array for the simpson's 1/3 rule approximations
    rombs = []  #array for the romberg integration approximations
    errs_t = [] #traps' corresponding errors
    errs_s = [] #simpsons' corresponding errors
    errs_r = [] #romberg integration errors
    for n in ns:
        if n < 1: continue
        T = composite_trapezoid(f, a, b, n)
        traps.append(T)
        errs_t.append(abs(T - true_val))
        if n % 2 == 1:
            # use n+1 for Simpson if odd, but keep ns consistent by skipping or using next even
            S = composite_simpson(f, a, b, n+1)
        else:
            S = composite_simpson(f, a, b, n) #for even n (simpson's rule requires even n)
        simps.append(S)
        errs_s.append(abs(S - true_val))
        R = romberg_integration(n,a,b,f)
        rombs.append(R)
        errs_r.append(abs(R-true_val))
    return (true_val, np.array(traps), np.array(simps), np.array(rombs), np.array(errs_t),
            np.array(errs_s), np.array(errs_r))

    #plotting the results:
def plot_results(ns, errs_t, errs_s, errs_r, true_val, traps, simps, rombs, title):
    fig, axes = plt.subplots(1,2, figsize=(12,4))
    ax = axes[0]
    ax.loglog(ns, errs_t, 'o-', label='Trapezoid error')
    ax.loglog(ns, errs_s, 's-', label='Simpson error')
    ax.loglog(ns, errs_r, 'r-', label='Romberg error')
    ax.set_xlabel('n (subintervals)')
    ax.set_ylabel('Absolute error')
    ax.set_title('Error vs n (log-log) — ' + title)
    ax.grid(True); ax.legend()

    ax2 = axes[1]
    ax2.plot(ns, traps, 'o-', label='Trapezoid approx')
    ax2.plot(ns, simps, 's-', label='Simpson approx')
    ax2.plot(ns, rombs, '.-', label='Romberg approx')
    ax2.axhline(true_val, color='k', ls='--', label='True value')
    ax2.set_xlabel('n (subintervals)')
    ax2.set_ylabel('Integral estimate')
    ax2.set_title('Approximate integral vs n')
    ax2.grid(True); ax2.legend()

    plt.tight_layout()
    plt.show()

    # estimate slopes (observed order) using last half of points
    def slope(ns, errs):
        i = max(1, len(ns)//2)
        p = np.polyfit(np.log(ns[i:]), np.log(errs[i:]), 1)
        return -p[0]  # slope = -order
    print("Observed order (Trapezoid):", slope(ns, errs_t))
    print("Observed order (Simpson):", slope(ns, errs_s))
    print("Observed order (Romberg):", slope(ns, errs_r))

# Example usage for three functions (ordered as function/f, a, b, title)
funcs = [
    (lambda x: np.exp(x), 2.0, 4.0, "exp(x) on [2,4]"),
    (lambda x: np.sin(x), 0.0, math.pi, "sin(x) on [0, pi]"),
    (lambda x: np.log(x), 2.0, 4.0, "log(x) on [2,4]"),
]

ns = [2**k for k in range(1,4)]  # n = 2,4,8,...,256 for testing accuracy of each approximation as n increases

for f,a,b,title in funcs:
    true_val, traps, simps, rombs, errs_t, errs_s, errs_r = convergence_study(f, a, b, ns)
    plot_results(ns, errs_t, errs_s, errs_r, true_val, traps, simps, rombs, title)