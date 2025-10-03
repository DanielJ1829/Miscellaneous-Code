import numpy as np
import matplotlib.pyplot as plt
#model: y = a*x + b  note x = x_data btw
#need to minimise: np.sum((y_data-y)**2)
# this happens when:
# b=(1/n)*sum(y_data[i]-a*x[i]), a = n*sum(x[i]*y_data[i])-sum(x[i])*sum(y_data[i])/n*sum(x[i]**2-(sum(x[i])^2
#(this is derived by minimising residuals with partial differentiation)


#initialise n here: (or just say n=len(x_data) for the length of your x data)
n=100
x = np.array([i for i in range(n)])
rng = np.random.default_rng(1323423)   #create random noise

def linear_regression(x,y_data):
    a = (n*np.sum(x*y_data)-np.sum(x)*np.sum(y_data))/(n*np.sum(x**2)-(np.sum(x))**2)
    b = (1/n)*np.sum(y_data-a*x)
    return a*x+b

def plotgird(k,c):
    fig, axes = plt.subplots(len(k), len(c), figsize=(15, 15))  #creates a figure and 2d array of axes
    fig.suptitle("y = k*x+c: fits for noisy data by c,k", fontsize=16)  #adds a large title for the whole figure
    y = np.zeros((len(k),len(c),n))
    y_data = np.zeros((len(k),len(c),n))
    for i in range(len(k)):
        for j in range(len(c)):
            y = c[j]+k[i]*x             #can hopefully generalise this so it says model(c,k,x) in future
            noise = rng.uniform(-3*k[i],3*k[i],size=n)  #adds random noise in (different for each y_data)
            y_data[i,j] = y + noise
            y_fit = linear_regression(x,y_data[i,j])            #again may be able to generalise this
            ax = axes[i,j]
            ax.scatter(x,y_data[i,j],alpha=0.5,s=9)   #alpha denotes the opacity of scatter points, s their size
            ax.plot(x,y_fit,linestyle = '-', color = 'black',label = "c={0}\n k={1}".format(c[j],k[i]))
            ax.legend(fontsize=10)
            # Remove axis ticks to keep the grid cleaner
            ax.set_xticks([])
            ax.set_yticks([])
    plt.tight_layout(rect=[0, 0, 1, 0.96])      #adjusts spacing between subplots so titles/plots don’t overlap
    plt.show()
k = [1,2,3,4,5]
c = [1,2,3,4,5]
plotgird(k,c)

