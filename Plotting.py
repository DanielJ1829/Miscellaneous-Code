import numpy as np
import matplotlib.pyplot as plt
import time
#circle:
'''radius = 1
numbers = []
X = np.linspace(-1, 1.5, 100)
Y = np.linspace(-1.5, 1.5, 100)

x,y = np.meshgrid(X, Y)     #it's this line
f = x**2 + y**2 - 2         #and this line that seem to be pretty important

plt.figure(figsize = (5,5))
plt.contour(x, y, f, levels = [0])    #levels tells you how many contours we want, in this case that's one.
plt.show()'''

X = np.linspace(-2, 0.5, 10000)
Y = np.linspace(-1.2, 1.2, 10000)
iterations = 100
bound = 2
function = lambda z, c: z**2 + c
iterray = []
time_i = time.time()
for x in X:
    row = []
    for y in Y:
        z = 0
        c = x + y*(1j)
        for i in range(iterations):
            if abs(z) >= bound:
                row.append(i)
                break
            else:
                try:
                    z = function(z, c)
                except (ValueError, ZeroDivisionError):
                    z = c
        else:
            row.append(0)
    iterray.append(row)
iterray = np.array(iterray)
iterray = iterray.T
time_f = time.time()
print('Time taken: {:.2f}'.format(time_f - time_i))


valid_cmaps = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Grays_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'berlin', 'berlin_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_grey', 'gist_grey_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg', 'gist_yerg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'grey_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'managua', 'managua_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'vanimo', 'vanimo_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
ax = plt.axes()
ax.set_aspect('equal')
n = np.random.randint(0, len(valid_cmaps)-1)
#graph = ax.pcolormesh(X, Y,  iterray, cmap = 'gist_ncar')
graph = plt.contourf(X, Y, iterray, cmap = 'bone')
plt.colorbar(graph)
plt.xlabel("Real Axis"), plt.ylabel("Imaginary Axis")
plt.title('Colour Scheme: bone')
#plt.savefig('C:/Users/danie/PycharmProjects/pythonProject/somethingelse.png', dpi = 3000)
plt.show()