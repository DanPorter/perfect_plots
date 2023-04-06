"""
Examples of good plotting practice

In this script, matplotlib is used with preferences set in plt.rc command

Including:
    1. Simple single plot figure with errorbars
    2. Figure with multiplots, 2nd axes split with left-and-right yaxes
    3. Plot with multiple lines, where colours are defined by a colormap
"""
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting

plt.rc('figure', figsize=(8, 6), dpi=100, autolayout=True)
plt.rc('lines', marker='o', color='r', linewidth=2, markersize=6)
plt.rc('errorbar', capsize=2)
plt.rc('legend', loc='best', frameon=False, fontsize=16)
plt.rc('axes', linewidth=2, titleweight='bold', labelsize='large')
plt.rc('xtick', labelsize='large')
plt.rc('ytick', labelsize='large')
plt.rc('axes.formatter', limits=(-3, 3), offset_threshold=6)
# Note font values appear to only be set when plt.show is called
plt.rc('font', family='serif', style='normal', weight='bold', size=16,
       serif=['Times New Roman', 'Times', 'DejaVu Serif'])
plt.rcParams["savefig.directory"] = os.path.dirname(__file__)  # Default save directory for figures
# plt.rcdefaults()

# Data
xdata = np.linspace(-180, 180, 100)
ydata = np.sin(np.radians(xdata))
ydata2 = np.cos(np.radians(xdata))

yerror = 0.1 * np.ones(len(ydata))

################Figure 1####################
# Simple figure with single axis           #
############################################
plt.figure()

plt.errorbar(xdata, ydata, yerror, label='sin')
plt.errorbar(xdata, ydata2, yerror, label='cos')

# Horizontal axis line
plt.axhline(0, color='k')

plt.xlim([-180, 180])
plt.ylim([-1.5, 1.5])

# axis labels
plt.legend()
plt.xlabel('Angle [Deg]')
plt.ylabel('Value')
plt.title('A Perfect Plot\n $y = \sin(x)$')
plt.savefig('plots/PerfectPlot_matplotlib_7', dpi=200)  # png

################Figure 2####################
# Figure with 2 subplots + overlapping axes#
############################################
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

# Figure 1 - Subplot 1 - Axes 1
plt.sca(ax1)
plt.text(-0.15, 1.07, '(a)', transform=plt.gca().transAxes)

plt.errorbar(xdata, ydata, yerror, label='sin')
plt.errorbar(xdata, ydata2, yerror, label='cos')

plt.xlim([-180, 180])
plt.ylim([-1.5, 1.5])

plt.legend()
plt.ylabel('Value')
plt.gca().get_yaxis().set_label_coords(-0.10, 0.5)

# plt.subplots_adjust(left=0.25)
plt.xticks([])  # No xticks on top figure

# Figure 1 - Subplot 2 - Axes 1
plt.sca(ax2)
plt.text(-0.15, 1.07, '(b)', transform=plt.gca().transAxes)

plt.plot(xdata, ydata, 'y-', label='sin')

plt.xlim([-180, 180])
plt.ylim([-1.5, 1.5])

plt.xlabel('Angle [Deg]')
plt.ylabel('sin')
plt.gca().get_yaxis().set_label_coords(-0.10, 0.5)

# Figure 1 - Subplot 2 - Axes 2
ax2b = ax2.twinx()  # Create axis ontop of ax2
plt.plot(xdata, ydata2 * 10, '-', ms=12, lw=4, label='sin')

plt.xlim([-180, 180])
plt.ylim([-15, 15])

plt.ylabel('10*cos')
plt.savefig('plots/PerfectPlot_matplotlib_8', dpi=200)  # png

################Figure 3####################
# Figure with colormapped plots            #
############################################
plt.figure()

# Colormaps: http://matplotlib.org/users/colormaps.html
cmap_name = 'viridis'
cm = plt.get_cmap(cmap_name)
# Note: cm(n) = (r,g,b,a)
#  if n = int, n = 0:255
#  if n = float, n = 0:1

datarange = np.arange(10, 101, 5, dtype=float)
colrange = (datarange - datarange[0]) / (datarange[-1] - datarange[0])
for n in range(len(datarange)):
    col = cm(colrange[n])  # add a small number here to keep values away from minimum colormap (white for hot_r)
    plt.plot(xdata, datarange[n] * ydata, '-', lw=2, color=col,
             label='%3.0f (%5.2f,%5.2f,%5.2f,%5.2f)' % (datarange[n], col[0], col[1], col[2], col[3]))

# Colorbar
sm = plt.cm.ScalarMappable(cmap=cm)
sm.set_array(datarange)
cbar = plt.colorbar(sm)
cbar.set_label('variation [unit]')

plt.xlabel('Angle [Deg]')
plt.ylabel('Value')
plt.title('%s' % cmap_name)
plt.savefig('plots/PerfectPlot_matplotlib_9', dpi=200)  # png

plt.show()
