import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Create some data
data_length = int(1e5)
x = np.random.normal(loc=1337, scale=80, size=data_length)
y = np.random.normal(loc=420, scale=50, size=data_length)

# Create a 2D histogram
histo, ex, ey = np.histogram2d(x, y, bins = (100, 100), range = [[1e3, 1.6e3], [2e2, 6e2]])

# Create a nice plot
plt.close('all')
inch_to_mm = 25.4
color = plt.cm.tab10

fig, ax = plt.subplots(2, 2, figsize=(80/inch_to_mm,60/inch_to_mm), sharex='col', sharey='row')
ax[0, 0].pcolormesh(ex, ey, histo.T, norm=LogNorm(), cmap='viridis', rasterized=True)

ax[0, 0].set_xlim(1e3, 1.6e3)
ax[0, 0].set_ylim(2e2, 6e2)

ax[0, 1].step(np.sum(histo, axis=0), ey[:-1], drawstyle='steps-post', linewidth=1, color=color(0))
ax[0, 1].fill_betweenx(ey[:-1], np.sum(histo, axis=0), 0, step='post', color=color(0), alpha=0.4, interpolate=True)

ax[1, 0].step(ex[:-1], np.sum(histo, axis=1), drawstyle='steps-post', linewidth=1, color=color(1))
ax[1, 0].fill_between(ex[:-1], np.sum(histo, axis=1), 0, step='pre', color=color(1), alpha=0.4, interpolate=True)

ax[1, 1].set_visible(False)
ax[1, 1].set_axis_off()
ax[0, 1].xaxis.set_tick_params(labelbottom=True)

plt.tight_layout(pad = 0.1)
fig.subplots_adjust(hspace=0, wspace=0)

save_name = 'create_nice_plot'
plt.savefig(f'{save_name}.jpg', dpi=300)
plt.savefig(f'{save_name}.pdf')

plt.show()
