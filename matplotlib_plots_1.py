"""
Examples of good plotting practice

In this script, matplotlib is used with preferences set inside the function calls

Including:
    1. Simple single plot figure with errorbars
    2. Figure with multiplots, 2nd axes split with left-and-right yaxes
    3. Plot with multiple lines, where colours are defined by a colormap
    4. 3D plot
    5. 2D surface colour plot
    6. Plot with inset axes
"""
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting

plt.rcParams["savefig.directory"] = os.path.dirname(__file__)  # Default save directory for figures

# Data
xdata = np.linspace(-180, 180, 100)
ydata = np.sin(np.radians(xdata))
ydata2 = np.cos(np.radians(xdata))

yerror = 0.1 * np.ones(len(ydata))

################ Figure 1 ####################
# Simple figure with single axis             #
##############################################
plt.figure(figsize=[12, 10], dpi=60)

plt.errorbar(xdata, ydata, yerror, fmt='g-o', markersize=12, linewidth=2, label='sin')
plt.errorbar(xdata, ydata2, yerror, fmt='m-s', markersize=12, linewidth=2, label='cos')

# Horizontal axis line
plt.axhline(0, color='k')

plt.xlim([-180, 180])
plt.ylim([-1.5, 1.5])

# axes border width
plt.setp(plt.gca().spines.values(), linewidth=2)

# axis labels
plt.legend(loc=0, frameon=False, prop={'size': 30, 'family': 'serif'})
plt.xlabel('Angle [Deg]', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.ylabel('Value', fontsize=32, fontweight='bold', fontstyle='italic', fontname='Times New Roman')
plt.title('A Perfect Plot\n $y = \sin(x)$', fontsize=32, fontweight='bold', fontname='Times New Roman')

# axis tick markers
plt.xticks(fontsize=25, fontname='Times New Roman')
plt.yticks(fontsize=25, fontname='Times New Roman')
plt.ticklabel_format(useOffset=False)
plt.ticklabel_format(style='sci', scilimits=(-3, 3))

# set border space outside axes
plt.subplots_adjust(left=0.15, bottom=0.12)
plt.savefig('plots/PerfectPlot_matplotlib_1', dpi=200)  # png
# plt.savefig('Perfect_Plot_1.pdf',dpi=300)  # pdf, eps, svg


################ Figure 2 ####################
# Figure with 2 subplots + overlapping axes  #
##############################################
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=[16, 12], dpi=60)

# Figure 1 - Subplot 1 - Axes 1
plt.sca(ax1)
plt.text(-0.15, 1.07, '(a)', transform=plt.gca().transAxes, fontsize=32, fontweight='bold',
         fontname='Times New Roman')  # (a)

plt.errorbar(xdata, ydata, yerror, fmt='g-o', markersize=12, linewidth=2, label='sin')
plt.errorbar(xdata, ydata2, yerror, fmt='m-s', markersize=12, linewidth=2, label='cos')

plt.xlim([-180, 180])
plt.ylim([-1.5, 1.5])

plt.legend(loc=0, frameon=False, prop={'size': 30, 'family': 'serif'})
plt.ylabel('Value', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.gca().get_yaxis().set_label_coords(-0.10, 0.5)

# plt.subplots_adjust(left=0.25)
plt.xticks([])  # No xticks on top figure
plt.yticks(fontsize=25, fontname='Times New Roman')

# Figure 1 - Subplot 2 - Axes 1
plt.sca(ax2)
plt.text(-0.15, 1.07, '(b)', transform=plt.gca().transAxes, fontsize=32, fontweight='bold',
         fontname='Times New Roman')  # (b)

plt.plot(xdata, ydata, 'y-', ms=12, lw=4, label='sin')

plt.xlim([-180, 180])
plt.ylim([-1.5, 1.5])

plt.xlabel('Angle [Deg]', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.ylabel('sin', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.gca().get_yaxis().set_label_coords(-0.10, 0.5)

# plt.subplots_adjust(left=0.25)
plt.xticks(fontsize=25, fontname='Times New Roman')
plt.yticks(fontsize=25, fontname='Times New Roman')

# Figure 1 - Subplot 2 - Axes 2
ax2b = ax2.twinx()  # Create axis ontop of ax2
plt.plot(xdata, ydata2 * 10, '-', ms=12, lw=4, label='sin')

plt.xlim([-180, 180])
plt.ylim([-15, 15])

plt.ylabel('10*cos', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.yticks(fontsize=25, fontname='Times New Roman')
plt.savefig('plots/PerfectPlot_matplotlib_2', dpi=200)  # png

################ Figure 3 ####################
# Figure with colormapped plots              #
##############################################
plt.figure(figsize=[12, 10], dpi=60)

# Colormaps: http://matplotlib.org/users/colormaps.html
# Spectral, summer, coolwarm, Wistia_r, pink_r, Set1, Set2, Set3, brg_r, Dark2, prism, PuOr_r, afmhot_r, 
# terrain_r, PuBuGn_r, RdPu, gist_ncar_r, gist_yarg_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r, 
# gist_stern, PuBu_r, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, 
# gist_heat_r, Wistia, OrRd_r, CMRmap, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, terrain, YlOrRd_r, 
# Set2_r, winter_r, PuBu, RdGy_r, spectral, rainbow, flag_r, jet_r, RdPu_r, gist_yarg, BuGn, Paired_r, hsv_r, 
# bwr, cubehelix, Greens, PRGn, gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, 
# Pastel1, gray_r, jet, Spectral_r, gnuplot2_r, gist_earth, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, 
# gnuplot_r, ocean_r, brg, gnuplot2, PuRd_r, bone_r, BuPu, Oranges, RdYlGn_r, PiYG, CMRmap_r, YlGn, binary_r,  
# gist_gray_r, Accent, BuPu_r, gist_gray, flag, bwr_r, RdBu_r, BrBG, Reds, Set1_r, summer_r, GnBu_r, BrBG_r, 
# Reds_r, RdGy, PuRd, Accent_r, Blues, autumn_r, autumn, cubehelix_r, nipy_spectral_r, ocean, PRGn_r, Greys_r, 
# pink, binary, winter, gnuplot, RdYlBu_r, hot, YlOrBr, coolwarm_r, rainbow_r, Purples_r, PiYG_r, YlGn_r, 
# Blues_r, YlOrBr_r, seismic, Purples, seismic_r, RdBu, Greys, BuGn_r, YlOrRd, PuOr, PuBuGn, nipy_spectral, afmhot
cmap_name = 'hot_r'
cm = plt.get_cmap(cmap_name)
# Note: cm(n) = (r,g,b,a)
#  if n = int, n = 0:255
#  if n = float, n = 0:1

# Alternate:
# cmap = plt.cm.copper
# plt.gca().set_color_cycle(cmap(np.linspace(0,1,len(datarange))))

datarange = np.arange(10, 101, 5, dtype=float)
colrange = (datarange - datarange[0]) / (datarange[-1] - datarange[0])
for n in range(len(datarange)):
    col = cm(colrange[n])  # add a small number here to keep values away from minimum colormap (white for hot_r)
    plt.plot(xdata, datarange[n] * ydata, '-', lw=2, color=col,
             label='%3.0f (%5.2f,%5.2f,%5.2f,%5.2f)' % (datarange[n], col[0], col[1], col[2], col[3]))

# Axes background colour
# plt.gca().set_facecolor('lightblue') # matplotlib 2.0+
plt.gca().patch.set_facecolor('lightblue')

# Colorbar
sm = plt.cm.ScalarMappable(cmap=cm)
sm.set_array(datarange)
cbar = plt.colorbar(sm)
cbar.set_label('variation [unit]', fontsize=24, fontweight='bold', fontname='Times New Roman')

# axis labels
# plt.legend(loc=0,fontsize=12,frameon=False)
plt.xlabel('Angle [Deg]', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.ylabel('Value', fontsize=32, fontweight='bold', fontstyle='italic', fontname='Times New Roman')
plt.title('%s' % cmap_name, fontsize=32, fontweight='bold', fontname='Times New Roman')

plt.setp(plt.gca().spines.values(), linewidth=2)
plt.xticks(fontsize=25, fontname='Times New Roman')
plt.yticks(fontsize=25, fontname='Times New Roman')
plt.ticklabel_format(useOffset=False)
plt.ticklabel_format(style='sci', scilimits=(-3, 3))
plt.subplots_adjust(left=0.15, bottom=0.12)
plt.savefig('plots/PerfectPlot_matplotlib_3', dpi=200)  # png


################ Figure 4 ####################
# Figure with 3D plots 	   	                 #
##############################################
fig = plt.figure(figsize=[12, 10], dpi=60)
ax = fig.add_subplot(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z ** 2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.view_init(elev=None, azim=220)
ax.set_xlim3d(-5, 5)
ax.set_ylim3d(-5, 5)
ax.set_zlim3d(-5, 5)
ax.set_xlabel('x', fontsize=22)
ax.set_ylabel('y', fontsize=22)
ax.set_zlabel('z', fontsize=22)
ax.set_title('Oh how lovely', fontsize=22)
ax.legend(loc=0, fontsize=30, frameon=False)
plt.savefig('plots/PerfectPlot_matplotlib_4', dpi=200)  # png


################ Figure 5 ####################
# Figure with pcolormesh                     #
##############################################
x = np.arange(-2, 2, 0.01)
y = np.arange(-3, 3, 0.05)
X, Y = np.meshgrid(x, y)
print('Meshgrid:')
print('X[:,0]: %s' % X[:, 0])
print('X[0,:]: %s' % X[0, :])
print('X.flatten()[:30] = %s' % X.flatten()[:30])
print('Y.flatten()[:30] = %s' % Y.flatten()[:30])
Z = 1 / (X ** 2 + Y ** 2)

plt.figure(figsize=[12, 10], dpi=60)
plt.pcolormesh(X, Y, Z, cmap='hot_r')
plt.axis('image')
plt.clim([0, 10])
cb = plt.colorbar()
plt.xlabel('Xdata', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.ylabel('Ydata', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.title('pcolormesh', fontsize=32, fontweight='bold', fontname='Times New Roman')
cb.set_label('Zdata', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.savefig('plots/PerfectPlot_matplotlib_5', dpi=200)  # png


################ Figure 6 ####################
# Figure with inset axes                     #
##############################################
cmap = plt.get_cmap('rainbow')
cols = cmap(np.linspace(0, 1, 6))

plt.figure(figsize=[10, 8], dpi=60)
plt.plot(xdata, ydata, 's-', ms=12, lw=4, c=cols[0], label='ydata')
plt.plot(xdata, ydata2, 's-', ms=12, lw=4, c=cols[1], label='ydata2')

plt.axvline(xdata[4], c='k', lw=1)
plt.legend(loc=1, frameon=False, fontsize=16, ncol=2, title='Ca$_2$Ru$_{1-x}$Mn$_{x}$O$_2$', title_fontsize=20)
plt.xlabel('T [K]', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.ylabel('Intensity [a. u.]', fontsize=32, fontweight='bold', fontname='Times New Roman')
plt.gca().get_yaxis().set_label_coords(-0.10, 0.5)
plt.yticks([])  # remove y ticks
plt.xticks(fontsize=25, fontname='Times New Roman')
plt.yticks(fontsize=25, fontname='Times New Roman')

# Inset axes
plt.axes([0.57, 0.42, 0.3, 0.3])
plt.pcolormesh(X, Y, Z)
plt.axis('image')
plt.clim([-1, 1])
plt.text(0.75, 0.8, '$\\frac{I_{(013)} - I_{(103)}}{I_{(013)} + I_{(103)}}$',
         transform=plt.gca().transAxes,
         ha='center',
         fontsize=18,
         fontname='Times New Roman',
         bbox=dict(facecolor='white', alpha=0.4, edgecolor='none', pad=0.2, boxstyle='round'),
         )
plt.xlabel('x || b* [\u00b5m]', fontsize=14, fontweight='bold', fontname='Times New Roman')
plt.ylabel('y || a* [\u00b5m]', fontsize=14, fontweight='bold', fontname='Times New Roman')
# plt.gca().get_yaxis().set_label_coords(-0.10,0.5)
plt.xticks(fontsize=10, fontname='Times New Roman')
plt.yticks(fontsize=10, fontname='Times New Roman')
plt.savefig('plots/PerfectPlot_matplotlib_6', dpi=200)  # png

plt.show()
