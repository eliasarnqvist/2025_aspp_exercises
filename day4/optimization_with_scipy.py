import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Import experimental and model data
data_exp = np.load('I_q_IPA_exp.npy')
data_exp = data_exp[~np.isnan(data_exp).any(axis=1)]
data_mod = np.load('I_q_IPA_model.npy')

# Scale model data to fit experimental data
data_mod_interp = np.interp(data_exp[:,0], data_mod[:,0], data_mod[:,1])
print(data_exp)

def scale(x, scale):
    """Scale input data by a constant"""
    return scale * data_mod_interp

popt, pcov = curve_fit(scale, data_exp[:,0], data_exp[:,1])
scaling_factor = popt[0]
data_mod_fitted = scale(data_exp[:,0], scaling_factor)

# Plot data
plt.close('all')
inch_to_mm = 25.4

# fig, ax = plt.subplots(figsize=(120/inch_to_mm,90/inch_to_mm))
# ax.plot(data_exp[:,0], data_exp[:,1], ls='-', marker='.', label='Experimental data')
# # ax.plot(data_mod[:,0], data_mod[:,1], label='Model data')
# ax.set_xlabel('Scattering vector')
# ax.set_ylabel('Scattering strength')
# ax.legend(frameon=False)

# fig, ax = plt.subplots(figsize=(120/inch_to_mm,90/inch_to_mm))
# # ax.plot(data_exp[:,0], data_exp[:,1], label='Experimental data')
# ax.plot(data_mod[:,0], data_mod[:,1], ls='-', marker='.', label='Model data')
# ax.plot(data_exp[:,0], data_mod_interp, ls='-', marker='.', label='Model data, interpolated')
# ax.set_xlabel('Scattering vector')
# ax.set_ylabel('Scattering strength')
# ax.legend(frameon=False)

fig, ax = plt.subplots(figsize=(120/inch_to_mm,90/inch_to_mm))
ax.plot(data_exp[:,0], data_exp[:,1], ls='-', lw=2, label='Experimental data')
ax.plot(data_exp[:,0], data_mod_fitted, ls='-', lw=2, label='Model data, scaled')
ax.set_xlabel('Scattering vector')
ax.set_ylabel('Scattering strength')
ax.legend(frameon=False)

save_name = 'plot_optimization'
plt.savefig(f'{save_name}.jpg', dpi=300)
plt.savefig(f'{save_name}.pdf')

plt.show()
